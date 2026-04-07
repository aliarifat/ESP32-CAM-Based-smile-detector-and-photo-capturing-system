import cv2
import urllib.request
import numpy as np

# ESP32-CAM URL
ESP32_CAM_URL = "http://192.168.1.103/cam-hi.jpg"

# Load Haar cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

def detect(gray, frame, original_frame): 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    for (x, y, w, h) in faces: 
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) 
        roi_gray = gray[y:y + h, x:x + w] 
        roi_color = frame[y:y + h, x:x + w] 
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20) 

        for (sx, sy, sw, sh) in smiles: 
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2) 
            print("Smile Detected! Capturing image...")

            # Save the original frame (without bounding boxes)
            cv2.imwrite("smile_detected.jpg", original_frame)

            # Show the captured image
            captured_image = cv2.imread("smile_detected.jpg")
            cv2.imshow("Captured Smile", captured_image)
            cv2.waitKey(2000)  # Display for 2 seconds
            cv2.destroyWindow("Captured Smile")
            
    return frame 

while True:
    try:
        # Fetch image from ESP32-CAM
        resp = urllib.request.urlopen(ESP32_CAM_URL)
        image_np = np.array(bytearray(resp.read()), dtype=np.uint8)
        frame = cv2.imdecode(image_np, -1)

        if frame is None:
            print("Failed to fetch image from ESP32-CAM")
            continue

        # Keep an unmodified copy of the frame for saving
        original_frame = frame.copy()

        # Convert to grayscale for detection					 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

        # Apply detection
        canvas = detect(gray, frame, original_frame) 

        # Display video feed with bounding boxes
        cv2.imshow('ESP32-CAM Video', canvas) 

        # Break loop when 'q' is pressed						 
        if cv2.waitKey(1) & 0xFF == ord('q'):			 
            break

    except Exception as e:
        print(f"Error: {e}")

# Release resources
cv2.destroyAllWindows()
