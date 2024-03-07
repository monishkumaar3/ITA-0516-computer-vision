import cv2

image = cv2.imread("download.jpeg")

resize_big = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

resize_small = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

cv2.imshow("Original ", image)

cv2.imshow("Bigger ", resize_big)

cv2.imshow("Smaller ", resize_small)

cv2.waitKey(0)

cv2.destroyAllWindows()
