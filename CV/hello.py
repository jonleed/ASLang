from flask import Flask, Response
import cv2
import os

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

# Route for video streaming
@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
