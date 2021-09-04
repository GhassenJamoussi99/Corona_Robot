from flask import Flask, render_template, Response
import cv2
from imutils.video import VideoStream
import imutils
import signal
import os

app = Flask(__name__)

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

vs = VideoStream(usePiCamera=1).start() 

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        global vs
        global faces
        OK = 0

        frame = vs.read()  # read the camera frame
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if os.path.exists('/tmp/prog1.pid'):
            OK = 1
            with open("/tmp/prog1.pid", "r") as pidfile:
                temp_pid = int(pidfile.readline())
 
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.5, 4)
        length = len(faces)
  
        if length != 0 and OK == 1:
            print(temp_pid)
            print("killing")
            os.kill(temp_pid, signal.SIGUSR1)
      
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        # concat frame one by one and show result
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  


@app.route('/video_feed')
def video_feed():
    #Video streaming route.
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def videostreaming():
    # start the flask app
    app.run(host="192.168.0.44",port=8000, debug=True,use_reloader=False)
