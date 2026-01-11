<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>

<body>

<h1>📏 Real-Time Finger Distance Measurement</h1>

<p><b>OpenCV</b> | <b>MediaPipe</b> | <b>Computer Vision</b></p>

<p>
Measure real-world distance in centimeters between two fingers using a camera.
This project performs live calibration using a physical ruler and tracks hand landmarks in real time.
</p>

<h2>🔥 Features</h2>
<ul>
    <li>Real-time hand tracking</li>
    <li>Pixel-to-centimeter calibration</li>
    <li>Live distance overlay</li>
    <li>Supports webcam, IP camera, phone camera</li>
    <li>Multi-threaded for smooth FPS</li>
</ul>

<h2>🧠 How It Works</h2>
<ol>
    <li>Place a ruler in front of the camera.</li>
    <li>Click the two ends of the ruler.</li>
    <li>System computes pixels-per-centimeter.</li>
    <li>Show two fingers to measure their distance in cm.</li>
</ol>

<h2>📦 Installation</h2>
<pre>
pip install opencv-python mediapipe numpy
</pre>

<h2>▶️ Run</h2>
<pre>
python main.py --url 0
</pre>

<p>Using phone camera:</p>

<pre>
python main.py --url http://192.168.1.10:8080/video --rul 32.75 --wid 680
</pre>

<h2>⚙️ Arguments</h2>
<ul>
    <li><b>--url</b> : Camera source (required)</li>
    <li><b>--rul</b> : Ruler length in cm (default 32.75)</li>
    <li><b>--wid</b> : Display width (default 680)</li>
</ul>

<h2>🖱 Calibration</h2>
<p>
Click two ends of the ruler on screen.  
Once calibrated, the system prints pixels-per-cm and starts live distance measurement.
</p>

<h2>🎥 Demo</h2>
<p>
Demo video included in repository showing calibration and real-time finger distance tracking.
</p>

<h2>🚀 Applications</h2>
<ul>
    <li>AR measurement tools</li>
    <li>Gesture recognition</li>
    <li>Robotics calibration</li>
    <li>Computer vision research</li>
</ul>

<h2>🔗 Connect</h2>
<ul>
    <li>YouTube: <a href="https://www.youtube.com/@Ethical-Monster" target="_blank">@Ethical-Monster</a></li>
    <li>Instagram: <a href="https://www.instagram.com/aarxv.shxrmx" target="_blank">@aarxv.shxrmx</a></li>
</ul>

<p>⭐ If you like this project, give it a star on GitHub.</p>

</body>
</html>
</ul>

<h2>🧠 How It Works</h2>
<ol>
    <li>Place a ruler in front of the camera.</li>
    <li>Click the two ends of the ruler.</li>
    <li>System computes pixels-per-centimeter.</li>
    <li>Show two fingers to measure their distance in cm.</li>
</ol>

<h2>📦 Installation</h2>
<pre>
pip install opencv-python mediapipe numpy
</pre>

<h2>▶️ Run</h2>
<pre>
python main.py --url 0
</pre>

<p>Using phone camera:</p>

<pre>
python main.py --url http://192.168.1.10:8080/video --rul 32.75 --wid 680
</pre>

<h2>⚙️ Arguments</h2>
<ul>
    <li><b>--url</b> : Camera source (required)</li>
    <li><b>--rul</b> : Ruler length in cm (default 32.75)</li>
    <li><b>--wid</b> : Display width (default 680)</li>
</ul>

<h2>🖱 Calibration</h2>
<p>
Click two ends of the ruler on screen.  
Once calibrated, the system prints pixels-per-cm and starts live distance measurement.
</p>

<h2>🎥 Demo</h2>
<p>
Demo video included in repository showing calibration and real-time finger distance tracking.
</p>

<h2>🚀 Applications</h2>
<ul>
    <li>AR measurement tools</li>
    <li>Gesture recognition</li>
    <li>Robotics calibration</li>
    <li>Computer vision research</li>
</ul>

<h2>👨‍💻 Author</h2>
<p>
Adeeb – Real-Time AI & Computer Vision Experiments
</p>

<h2>🔗 Connect With Me</h2>
<ul>
    <li>YouTube: <a href="https://www.youtube.com/@Ethical-Monster" target="_blank">@Ethical-Monster</a></li>
    <li>Instagram: <a href="https://www.instagram.com/aarxv.shxrmx" target="_blank">@aarxv.shxrmx</a></li>
</ul>

<p>⭐ If you like this project, give it a star on GitHub.</p>

</body>
</html>
    font-size:14px;
}
.section{
    margin-top:30px;
}
ul{
    margin-left:20px;
}
.footer{
    text-align:center;
    margin-top:40px;
    color:#8b949e;
    font-size:14px;
}
.highlight{
    color:#f778ba;
}
</style>
</head>

<body>
<div class="container">

<h1>📏 Real-Time Finger Distance Measurement</h1>
<div class="badge">OpenCV</div>
<div class="badge">MediaPipe</div>
<div class="badge">Computer Vision</div>

<p>
Measure <span class="highlight">real-world distance in centimeters</span> between two fingers using a camera.
This project performs live calibration using a physical ruler and tracks hand landmarks in real time.
</p>

<div class="section">
<h2>🔥 Features</h2>
<ul>
    <li>Real-time hand tracking</li>
    <li>Pixel-to-centimeter calibration</li>
    <li>Live distance overlay</li>
    <li>Supports webcam, IP camera, phone camera</li>
    <li>Multi-threaded for smooth FPS</li>
</ul>
</div>

<div class="section">
<h2>🧠 How It Works</h2>
<ol>
    <li>Place a ruler in front of the camera.</li>
    <li>Click the two ends of the ruler.</li>
    <li>System computes pixels-per-centimeter.</li>
    <li>Show two fingers to measure their distance in cm.</li>
</ol>
</div>

<div class="section">
<h2>📦 Installation</h2>
<div class="code">
pip install opencv-python mediapipe numpy
</div>
</div>

<div class="section">
<h2>▶️ Run</h2>
<div class="code">
python main.py --url 0
</div>
<p>Using phone camera:</p>
<div class="code">
python main.py --url http://192.168.1.10:8080/video --rul 32.75 --wid 680
</div>
</div>

<div class="section">
<h2>⚙️ Arguments</h2>
<ul>
    <li><b>--url</b> : Camera source (required)</li>
    <li><b>--rul</b> : Ruler length in cm (default 32.75)</li>
    <li><b>--wid</b> : Display width (default 680)</li>
</ul>
</div>

<div class="section">
<h2>🖱 Calibration</h2>
<p>
Click two ends of the ruler on screen.  
Once calibrated, the system prints pixels-per-cm and starts live distance measurement.
</p>
</div>

<div class="section">
<h2>🎥 Demo</h2>
<p>
Demo video included in repository showing calibration and real-time finger distance tracking.
</p>
</div>

<div class="section">
<h2>🚀 Applications</h2>
<ul>
    <li>AR measurement tools</li>
    <li>Gesture recognition</li>
    <li>Robotics calibration</li>
    <li>Computer vision research</li>
</ul>
</div>

<div class="section">
<h2>👨‍💻 Author</h2>
<p>
Adeeb – Real-Time AI & Computer Vision Experiments
</p>
</div>

<div class="footer">
⭐ If you like this project, give it a star on GitHub.
</div>

</div>
</body>
</html>
