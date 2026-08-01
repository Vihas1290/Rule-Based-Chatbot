import cv2

image = cv2.imread('image.png')

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

def main():
    cv2.resizeWindow('Image', 800, 600)

    cv2.imshow('Image', image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

cv2.waitKey(0)

main()

