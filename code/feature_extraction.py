import cv2
import numpy as np

# Define paths based on the project structure
image_path = "fingerprint_dataset/real_data/00001.bmp"

# Load a sample fingerprint image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Thresholding: Convert the image to binary
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Edge Detection: Use Canny edge detector
edges = cv2.Canny(image, 100, 200)

# Visualize the results
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary_image)
cv2.imshow("Edges", edges)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
