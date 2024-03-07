import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Calculate histograms for each channel
    hist_blue = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_green = cv2.calcHist([image], [1], None, [256], [0, 256])
    hist_red = cv2.calcHist([image], [2], None, [256], [0, 256])

    # Plot histograms
    plt.figure(figsize=(10, 6))
    plt.plot(hist_blue, color='b', label='Blue')
    plt.plot(hist_green, color='g', label='Green')
    plt.plot(hist_red, color='r', label='Red')
    plt.title('Histogram of RGB channels')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()

# Example usage
analyze_histogram('download.jpeg')
