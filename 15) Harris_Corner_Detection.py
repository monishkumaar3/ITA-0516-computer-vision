import cv2
import numpy as np

image = cv2.imread("download.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

threshold = 0.01 * dst.max()

corner_image = np.zeros_like(image)

corner_image[dst > threshold] = [0, 0, 255]

cv2.imshow("Corners Detected", corner_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
