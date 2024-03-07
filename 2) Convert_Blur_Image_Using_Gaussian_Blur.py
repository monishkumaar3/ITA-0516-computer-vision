import cv2

image = cv2.imread("download.jpeg")

cv2.imshow("Original_Image", image)

blurred_image = cv2.GaussianBlur(image, (9,9),0)

cv2.imshow("Blurred Image", blurred_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
