import cv2
import mediapipe as mp
import threading
import time
import argparse
import numpy as np
import math

def getDist(p1,p2):
    dx=p1[0]-p2[0]
    dy=p1[1]-p2[1]
    return math.sqrt(dx*dx+dy*dy)

class camera:
    def __init__(self,url):
        self.video=cv2.VideoCapture(url)
        self.video.set(cv2.CAP_PROP_BUFFERSIZE,1)
        self.running=False
        self.frame=None
        self.thread=threading.Thread(target=self.readLoop,daemon=True)

    def startCam(self):
        self.running=True
        self.thread.start()
        return self

    def readLoop(self):
        while self.running:
            success,img=self.video.read()
            if not success:
                break
            self.frame=img

    def getFrame(self):
        return self.frame

    def stopCam(self):
        self.running=False
        self.video.release()

class handTrack:
    def __init__(self):
        self.model=mp.solutions.hands.Hands(False,2,0,0.5,0.5)
        self.result=None
        self.inputFrame=None
        self.running=False
        self.thread=threading.Thread(target=self.workLoop,daemon=True)

    def startTrack(self):
        self.running=True
        self.thread.start()
        return self

    def workLoop(self):
        while self.running:
            if self.inputFrame is not None:
                rgb=cv2.cvtColor(self.inputFrame,cv2.COLOR_BGR2RGB)
                self.result=self.model.process(rgb)
                self.inputFrame=None
            else:
                time.sleep(0.01)

    def stopTrack(self):
        self.running=False
        self.model.close()

calPoints=[]
pixelsPerCm=None
realRulerLen=32.75

def mouse(event,x,y,flags,param):
    global calPoints,pixelsPerCm
    if event==cv2.EVENT_LBUTTONDOWN and len(calPoints)<2:
        calPoints.append((x,y))
        if len(calPoints)==2:
            d=getDist(calPoints[0],calPoints[1])
            pixelsPerCm=d/realRulerLen
            print("Calibrated:",pixelsPerCm,"pixels/cm")

def main():
    global realRulerLen

    parser=argparse.ArgumentParser()
    parser.add_argument("--url",type=str,required=True)
    parser.add_argument("--rul",type=float,default=32.75)
    parser.add_argument("--ch",type=float,default=50.0)
    parser.add_argument("--hh",type=float,default=4.0)
    parser.add_argument("--wid",type=int,default=680)
    args=parser.parse_args()

    realRulerLen=args.rul

    cam=camera(args.url).startCam()
    hands=handTrack().startTrack()

    cv2.namedWindow("Real time Distance")
    cv2.setMouseCallback("Real time Distance",mouse)

    try:
        while True:
            frame=cam.getFrame()
            if frame is None:
                continue

            h,w=frame.shape[:2]
            scale=args.wid/w
            frame=cv2.resize(frame,(args.wid,int(h*scale)))
            fh,fw=frame.shape[:2]

            if hands.inputFrame is None:
                hands.inputFrame=frame

            for p in calPoints:
                cv2.circle(frame,p,6,(0,0,255),-1)
            if len(calPoints)==2:
                cv2.line(frame,calPoints[0],calPoints[1],(255,0,0),2)

            points=[]
            if hands.result and hands.result.multi_hand_landmarks:
                for hand in hands.result.multi_hand_landmarks:
                    tip=hand.landmark[8]
                    points.append((int(tip.x*fw),int(tip.y*fh)))

            if len(points)>=2 and pixelsPerCm is not None:
                p1,p2=points[0],points[1]
                pixelDist=getDist(p1,p2)
                cm=pixelDist/pixelsPerCm

                cv2.line(frame,p1,p2,(0,255,0),3)
                cv2.circle(frame,p1,5,(0,0,255),-1)
                cv2.circle(frame,p2,5,(0,0,255),-1)
                cv2.putText(frame,f"{cm:.2f} cm",(p1[0],p1[1]-15),
                           cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

            if pixelsPerCm is None:
                cv2.putText(frame,f"Click 2 ends of {args.rul}cm ruler",
                           (20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

            cv2.imshow("Real time Distance",frame)

            if cv2.waitKey(1)&0xFF==ord('q'):
                break

    finally:
        cam.stopCam()
        hands.stopTrack()
        cv2.destroyAllWindows()

if __name__=="__main__":
    main()
