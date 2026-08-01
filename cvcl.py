import cv2

image = cv2.imread("image.png")

cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_image.png", image)

sizes = [(400, 400), (500, 500), (600, 600)]
for size in sizes:
    resized_image = cv2.resize(image, size)
    cv2.imshow(f"Resized Image {size}", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()