import cv2
from fer import FER

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Emotion detector
emotion_detector = FER(mtcnn=False)

# Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera.")
    raise SystemExit

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not capture frame.")
        break

    # Convert to grayscale for OpenCV face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Check every face
    for x, y, w, h in faces:

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        # Crop face
        face = frame[y:y+h, x:x+w]

        try:
            # Detect emotion
            emotion, score = emotion_detector.top_emotion(face)

            if emotion is not None:

                text = f"{emotion.capitalize()} {score * 100:.0f}%"

                cv2.putText(
                    frame,
                    text,
                    (x, max(y - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

        except Exception as e:
            print("Emotion error:", e)

    # People count
    cv2.putText(
        frame,
        f"People Count: {len(faces)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    # Display
    cv2.imshow(
        "Face Detection + Emotion Detection",
        frame
    )

    # Q = Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()