import cv2

source_image = cv2.imread('download.jpeg')

x, y, width, height = cv2.selectROI('Source Image', source_image)
roi = source_image[y:y+height, x:x+width]

canvas = source_image.copy()
canvas[y:y+height, x:x+width] = roi

cv2.imshow('Pasted ROI', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('pasted_roi_image.jpg', canvas)
