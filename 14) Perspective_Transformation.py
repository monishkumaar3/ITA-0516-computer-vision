import cv2
import numpy as np

image = cv2.imread("download.jpeg")

src = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])

dst = np.float32([[0,0], [300,0], [0,300], [300,300]])

m = cv2.getPerspectiveTransform(src, dst)

tranform_im = cv2.warpPerspective(image, m, (300, 300))

cv2.imshow("Original", image)

cv2.imshow("Transformed", tranform_im)

cv2.waitKey(0)

cv2.destroyAllWindows()
