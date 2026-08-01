import cv2
import matplotlib.pyplot as plt


image = cv2.imread("image.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, _ = image_rgb.shape

rect_width1 = 20
rect_height1 = 20
top_left1 = (65, int(40.5))
bottom_right1 = (top_left1[0] + rect_width1, top_left1[1] + rect_height1)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (230, 120, 100), 2)

rect_width2 = 20
rect_height2 = 20
top_left2 = (95, int(40.5))
bottom_right2 = (top_left2[0] + rect_width2, top_left2[1] + rect_height2)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (230, 120, 100), 2)

rect_width3 = 20
rect_height3 = 1
top_left3 = (80, int(40.5))
bottom_right3 = (top_left3[0] + rect_width3, top_left3[1] + rect_height3)
cv2.rectangle(image_rgb, top_left3, bottom_right3, (230, 120, 100), 2)

center_x = top_left1[0] + rect_width1 // 2
center_y = top_left1[1] + rect_height1 // 2

center_x2 = top_left2[0] + rect_width2 // 2
center_y2 = top_left2[1] + rect_height2 // 2

cv2.line(image_rgb, (center_x, center_y), (center_x2, center_y2), (0, 255, 0), 2)

cv2.putText(image_rgb, "Potato with Glasses", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (222, 119, 7), 1)

arrow_start = (int(1
                   ), int(132.5))
arrow_end = (int(174), int(132.5))
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (0, 0, 255), 2)
cv2.putText(image_rgb, "1 to 174", (int(arrow_start[0] + 5), int(arrow_start[1] - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

plt.title("Image with Rectangle")
plt.imshow(image_rgb)
plt.show()