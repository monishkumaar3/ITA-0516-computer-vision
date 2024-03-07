import cv2

image = cv2.imread("download.jpeg", cv2.IMREAD_GRAYSCALE)

equ_im = cv2.equalizeHist(image)

cv2.imshow("Original_Image", image)

cv2.imshow("Equalized Image", equ_im)

cv2.waitKey(0)

cv2.destroyAllWindows()
