import cv2
import numpy as np

width = int(input("Enter the width of the image : "))
height = int(input("Enter the height of the image : "))

white_image = np.ones((height, width),  np.uint8)*255

start_point = (int(width*0.25), int(height*0.25))  # Top-left corner
end_point = (int(width*0.75), int(height*0.75))    # Bottom-right corner
color = (0, 0, 255)  # Red color in BGR format
thickness = 2

rect = cv2.rectangle(white_image, start_point, end_point, color, thickness)

cv2.imshow("Rectangle", rect)
cv2.waitKey(0)
cv2.destroyAllWindows()
