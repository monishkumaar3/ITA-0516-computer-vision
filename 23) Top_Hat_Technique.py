import cv2
import numpy as np

input_image = cv2.imread('download.jpeg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)

opened_image = cv2.morphologyEx(input_image, cv2.MORPH_OPEN, kernel)

tophat_image = cv2.subtract(input_image, opened_image)

cv2.imshow('Original Image', input_image)
cv2.imshow('Top Hat Image', tophat_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
