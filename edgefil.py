import cv2
import questionary
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    plt.figure(figsize = (8,8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image_rgb)
    plt.title(title)
    plt.axis('off')
    plt.show()
    
def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Grayscale Image", gray_image)
    
    while True:
        method = questionary.select(
        "Choose an edge detection method:",
        choices=[
            "Canny",
            "Sobel",
            "Scharr",
            "Laplacian",
            "Gaussian Smoothing",
            "Median Filtering",
            "Exit"
        ]
    ).ask()
    
        if method == "Sobel":
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
            combined_sobel = cv2.magnitude(sobel_x, sobel_y)
            display_image("Sobel Edge Detection", combined_sobel)
            
        elif method == "Scharr":
            scharr_x = cv2.Scharr(gray_image, cv2.CV_64F, 1, 0)
            scharr_y = cv2.Scharr(gray_image, cv2.CV_64F, 0, 1)
            combined_scharr = cv2.magnitude(scharr_x, scharr_y)
            normalized_scharr = np.uint8(255 * combined_scharr / np.max(combined_scharr))
            display_image("Scharr Edge Detection", normalized_scharr)
            
        elif method == "Canny":
            low_threshold = questionary.text("Enter low threshold for Canny (default 100):", default="100").ask()
            high_threshold = questionary.text("Enter high threshold for Canny (default 200):", default="200").ask()
            try:
                low_threshold = int(low_threshold)
                high_threshold = int(high_threshold)
            except ValueError:
                print("Invalid input. Using default thresholds.")
                low_threshold = 100
                high_threshold = 200
            edges = cv2.Canny(gray_image, low_threshold, high_threshold)
            display_image("Canny Edge Detection", edges)
        
        elif method == "Laplacian":
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))
        elif method == "Gaussian Smoothing":
            kernel_size = questionary.text("Adjust kernel size for Gaussian Smoothing (odd number, default 5):", default="5").ask()
            try:
                kernel_size = int(kernel_size)
                if kernel_size % 2 == 0:
                    print("Kernel size must be an odd number. Using default value 5.")
                    kernel_size = 5
            except ValueError:
                print("Invalid input. Using default kernel size 5.")
                kernel_size = 5
            smoothed_image = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), 0)
            display_image("Gaussian Smoothing", smoothed_image)
        elif method == "Median Filtering":
            kernel_size = questionary.text("Adjust kernel size for Median Filtering (odd number, default 5):", default="5").ask()
            try:
                kernel_size = int(kernel_size)
                if kernel_size % 2 == 0:
                    print("Kernel size must be an odd number. Using default value 5.")
                    kernel_size = 5
            except ValueError:
                print("Invalid input. Using default kernel size 5.")
                kernel_size = 5
            filtered_image = cv2.medianBlur(gray_image, kernel_size)
            display_image("Median Filtering", filtered_image)
        elif method == "Exit":
            print("Exiting the program.")
            break
    
interactive_edge_detection("image.png")