import cv2

image = cv2.imread("download.jpeg")

transposed_image = cv2.transpose(image)

rotated_image = cv2.flip(transposed_image,1)

cv2.imshow("Original", image)

cv2.imshow("Rotated", rotated_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
