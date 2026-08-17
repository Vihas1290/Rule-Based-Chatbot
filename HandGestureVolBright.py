import cv2
import numpy as np
import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# FIXED IMPORT: This pulls the exact Enum class containing THUMB_TIP and INDEX_FINGER_TIP
from mediapipe.tasks.python.vision.hand_landmarker import HandLandmark

# System controls libraries
from pycaw.pycaw import AudioUtilities
import screen_brightness_control as sbc

# =====================================================================
# 1. PYCAW INITIALIZATION (Audio Control)
# =====================================================================
try:
    devices = AudioUtilities.GetSpeakers()
    volume = devices.EndpointVolume
    
    vol_range = volume.GetVolumeRange()  # returns (min_vol, max_vol, step)
    min_vol = vol_range[0]
    max_vol = vol_range[1]
except Exception as e:
    print(f"Error initializing system audio: {e}")
    volume = None
    min_vol, max_vol = -65.25, 0.0

# =====================================================================
# 2. CONVERTED MEDIAPIPE 3.11+ TASKS CONFIGURATION
# =====================================================================
Hands = vision.HandLandmarker

# FIXED: Successfully maps indices using the explicitly imported Enum
TH = HandLandmark.THUMB_TIP         # Value: 4
IX = HandLandmark.INDEX_FINGER_TIP  # Value: 8

# Configure Options Structure
# Make sure 'hand_landmarker.task' is downloaded and in your script directory!
options = vision.HandLandmarkerOptions(
    base_options=python.BaseOptions(model_asset_path='hand_landmarker.task'),
    running_mode=vision.RunningMode.IMAGE, 
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7
)
hands = Hands.create_from_options(options)

# Helper function to custom draw hand joints since mp.solutions is deprecated
def draw_hand_connections(img, landmarks, w, h):
    connections = [
        (0, 1), (1, 2), (2, 3), (3, 4),        # Thumb
        (0, 5), (5, 6), (6, 7), (7, 8),        # Index Finger
        (5, 9), (9, 10), (10, 11), (11, 12),   # Middle Finger
        (9, 13), (13, 14), (14, 15), (15, 16), # Ring Finger
        (13, 17), (17, 18), (18, 19), (19, 20), (0, 17) # Pinky & Palm
    ]
    
    # Draw tracking links
    for connection in connections:
        pt1 = landmarks[connection[0]]
        pt2 = landmarks[connection[1]]
        x1, y1 = int(pt1.x * w), int(pt1.y * h)
        x2, y2 = int(pt2.x * w), int(pt2.y * h)
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
    # Draw individual joint nodes
    for lm in landmarks:
        cx, cy = int(lm.x * w), int(lm.y * h)
        cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)

# =====================================================================
# 3. CAMERA INFERENCE LOOP
# =====================================================================
cap = cv2.VideoCapture(0)

print("Starting tracking loop. Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    detection_result = hands.detect(mp_image)

    if detection_result.hand_landmarks:
        for hand_landmarks in detection_result.hand_landmarks:
            
            draw_hand_connections(frame, hand_landmarks, w, h)
            
            thumb_lm = hand_landmarks[TH]
            index_lm = hand_landmarks[IX]

            x1, y1 = int(thumb_lm.x * w), int(thumb_lm.y * h)
            x2, y2 = int(index_lm.x * w), int(index_lm.y * h)
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            cv2.circle(frame, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(frame, (cx, cy), 8, (255, 255, 0), cv2.FILLED)

            distance = math.hypot(x2 - x1, y2 - y1)

            # ---------------------------------------------------------
            # GESTURE ACTUATOR LOGIC
            # ---------------------------------------------------------
            if volume is not None:
                target_vol = np.interp(distance, [20, 200], [min_vol, max_vol])
                try:
                    volume.SetMasterVolumeLevel(target_vol, None)
                except Exception:
                    pass

            target_bright = np.interp(distance, [20, 200], [0, 100])
            try:
                sbc.set_brightness(int(target_bright))
            except Exception:
                pass

            vol_bar = np.interp(distance, [20, 200], [400, 150])
            cv2.rectangle(frame, (50, 150), (85, 400), (0, 255, 0), 3)
            cv2.rectangle(frame, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, f'VAL: {int(target_bright)}%', (40, 430), 
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Hand Gesture Volume & Brightness Control", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
