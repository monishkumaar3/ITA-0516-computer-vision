import cv2

# Read the image
image = cv2.imread("download.jpeg")

# Get text input from the user
text = input("Enter the text to be displayed on the image: ")

# Overlay the text on the image
cv2.putText(image, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Display the image with the text
cv2.imshow('Image with Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
