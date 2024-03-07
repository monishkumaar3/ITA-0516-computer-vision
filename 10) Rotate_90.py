import cv2

image = cv2.imread("download.jpeg")

flipped_image = cv2.flip(image, 1)

rotated_image = cv2.transpose(flipped_image)

cv2.imshow("Original ", image)

cv2.imshow("Rotated ", rotated_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
