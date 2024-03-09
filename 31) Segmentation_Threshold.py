import cv2

image = cv2.imread("download.jpeg")
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Prompt the user for lower and upper threshold values
lower_threshold = int(input("Enter the lower threshold value: "))
upper_threshold = int(input("Enter the upper threshold value: "))

# Apply thresholding to segment the image
_, segmented_image = cv2.threshold(grayscale_image, lower_threshold, upper_threshold, cv2.THRESH_BINARY)

# Display the segmented image
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
