import cv2
import numpy as np

input_image = cv2.imread('download.jpeg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)

closed_image = cv2.morphologyEx(input_image, cv2.MORPH_CLOSE, kernel)

blackhat_image = cv2.subtract(closed_image, input_image)

cv2.imshow('Original Image', input_image)
cv2.imshow('Black Hat Image', blackhat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
