from deepface import DeepFace
import cv2
import os

KNOWN_FACES_DIR = "known_faces"

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("[INFO] Starting real-time face recognition...")
print("[INFO] Press 'ESC' to quit.")

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame.")
        break

    try:
        result = DeepFace.find(
            img_path=frame,
            db_path=KNOWN_FACES_DIR,
            enforce_detection=True,
            detector_backend='mtcnn'  # Try opencv, retinaface, mediapipe, ssd, etc.
        )

        print("[INFO] Detection Result:", result)

        if len(result) > 0 and not result[0].empty:
            best_match = result[0].iloc[0]
            identity_path = best_match["identity"]
            identity_name = os.path.splitext(os.path.basename(identity_path))[0]

            label = f"Match: {identity_name}"
            color = (0, 255, 0)
        else:
            label = "No Match Found"
            color = (0, 0, 255)

    except Exception as e:
        label = "Face not detected"
        color = (0, 0, 255)
        print("[ERROR]", e)

    cv2.putText(frame, label, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Face Recognition - DeepFace", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
