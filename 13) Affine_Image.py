import cv2
import numpy as np

image = cv2.imread("download.jpeg")

m = np.float32([[1,0,100], [0,1,50]])

tranform_image = cv2.warpAffine(image, m, (image.shape[1], image.shape[0]))

cv2.imshow("Original", image)

cv2.imshow("Transformed", tranform_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
