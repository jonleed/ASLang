'''from flask import Flask, Response
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time

app = Flask(__name__)

# Open the default camera (webcam)
cap = cv2.VideoCapture(0)


# Function to generate video frames
def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

def captureframe():
    # Open the default camera (webcam)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Display the frame in a window named 'Video'
        cv2.imshow('Video', frame)

        # Check for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the video window
    cap.release()
    cv2.destroyAllWindows()
# Route for video streaming
@app.route('/video')
def video(): 
    captureframe()
    return  Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")


detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

offset = 20
imgSize = 300

labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

while True:
    try:
        success, img = cap.read()
        hands, img = detector.findHands(img)
        imgOutput = img.copy()
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox'] ## Bounding Box

            # Isolate box around hand
            imgBlack = np.ones((imgSize, imgSize, 3), np.uint8)*255
            imgCrop = img[y-offset : y+h+offset , x-offset : x+w+offset]
            imgCropShape = imgCrop.shape
        
        
            # Fill the screen with smaller images
            aspectRatio = h/w

            if aspectRatio > 1:
                k = imgSize/h
                wCal = math.ceil(k*w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize)) 
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal)/2)
                imgBlack[ :, wGap:wCal+wGap] = imgResize
                prediction, index = classifier.getPrediction(imgBlack, draw=False)
                #print(prediction, index)

            else: 
                k = imgSize/w
                hCal = math.ceil(k*h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal)) 
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal)/2)
                imgBlack[ hGap:hCal+hGap, :] = imgResize
                prediction, index = classifier.getPrediction(imgBlack, draw=False)
            
                #print(prediction, index)


            cv2.putText(imgOutput, labels[index], (x+80, y-30), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)

            #cv2.imshow("ImageCrop", imgCrop)
            #cv2.imshow("ImageBlack", imgBlack)


        #cv2.imshow("Image", imgOutput)
        key = cv2.waitKey(1)
    except:
        pass'''

from flask import Flask, Response
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
from flask_socketio import SocketIO
import time

app = Flask(__name__)

# Open the default camera (webcam)
cap = cv2.VideoCapture(0)

socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")

# Function to generate video frames
def generate_frames():
    detector = HandDetector(maxHands=1)
    classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

    offset = 20
    imgSize = 300

    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Perform hand tracking
        hands, img = detector.findHands(frame)

        # Perform hand classification
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']

            # Isolate box around hand
            imgBlack = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            imgCrop = img[y-offset : y+h+offset , x-offset : x+w+offset]
            imgCropShape = imgCrop.shape

            # Fill the screen with smaller images
            aspectRatio = h/w

            if aspectRatio > 1:
                k = imgSize/h
                wCal = math.ceil(k*w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal)/2)
                imgBlack[ :, wGap:wCal+wGap] = imgResize
                prediction, index = classifier.getPrediction(imgBlack, draw=False)
            else:
                k = imgSize/w
                hCal = math.ceil(k*h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal)/2)
                imgBlack[ hGap:hCal+hGap, :] = imgResize
                prediction, index = classifier.getPrediction(imgBlack, draw=False)

            cv2.putText(frame, labels[index], (x+80, y-30), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)

        ret, buffer = cv2.imencode('.jpeg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@app.route('/video')
def video():
    print('things happened')
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")
    #app.run(debug=True, host="0.0.0.0")
