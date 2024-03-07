import cv2

original_image = cv2.imread('download.jpeg')
watermark_image = cv2.imread('download (1).jpeg', cv2.IMREAD_UNCHANGED)

watermark_resized = cv2.resize(watermark_image, (original_image.shape[1], original_image.shape[0]))

alpha = 0.5
watermarked_image = cv2.addWeighted(original_image, 1 - alpha, watermark_resized, alpha, 0)

cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('watermarked_image.jpg', watermarked_image)
