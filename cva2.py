import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("image.png")

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Gray Image")
plt.show()

cropped_image = image[10:150, 10:100]
plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
plt.title("Cropped Image")
plt.show()

(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))
plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.title("Rotated Image")
plt.show()

brighter_matrix = np.ones(image.shape, dtype="uint8") * 50.00008
brighter_image = cv2.add(image, brighter_matrix)
plt.imshow(cv2.cvtColor(brighter_image, cv2.COLOR_BGR2RGB))
plt.title("Brighter Image")
plt.show()