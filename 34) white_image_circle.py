import cv2
import numpy as np

width = int(input("Enter the width of the image : "))
height = int(input("Enter the height of the image : "))

white_image = np.ones((height, width), np.uint8) * 255

center = (int(width / 2), int(height / 2))  # Center of the circle
radius = min(width, height) // 4  # Radius of the circle
color = (0, 0, 255)  # Red color in BGR format
thickness = 2

circle_img = cv2.circle(white_image, center, radius, color, thickness)

cv2.imshow("Circle", circle_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
