import cv2
import numpy as np

image = cv2.imread("download.jpeg", cv2.IMREAD_GRAYSCALE)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize = 3)
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
cv2.imshow('Sobel Filtered Image', sobel_combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
