import cv2
import numpy as np

def apply_filter(img, filter_type):
    img = img.copy()

    if img is None:
        raise ValueError("Input image is None")

    if filter_type == "red_tint":
        img[:, :, 1] = img[:, :, 0] = 0  # Zero out the blue and green channels
        return img
    elif filter_type == "blue_tint":
        img[:, :, 0] = img[:, :, 2] = 0  # Zero out the red and green channels
        return img
        
    elif filter_type == "edge":
        img[:, :, 1] = img[:, :, 2] = 0  # Zero out the green and red channels
        return img
    elif filter_type == "sobel":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
        sobel = cv2.magnitude(sobelx, sobely)
        sobel = cv2.convertScaleAbs(sobel)
        return cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)
    elif filter_type == "cartoon":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(img, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return cartoon
    elif filter_type == "pencil_sketch":
        gray, sketch = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
        return sketch

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        filter_type = "original"  
        if filter_type == "original":
            filtered_frame = frame
        elif filter_type in ["red_tint", "blue_tint", "edge", "sobel", "cartoon", "pencil_sketch"]:
            filtered_frame = apply_filter(frame, filter_type)
        else:
            filtered_frame = frame

        cv2.imshow('Filtered Frame', filtered_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()