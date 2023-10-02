import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Define paths based on the project structure
dataset_path = "fingerprint_dataset/real_data/"
image_path = None

# Get a list of all the images in the dataset
image_names = os.listdir(dataset_path)

# Display the list of images to the user
print("Select an image from the following list:")
for i, image_name in enumerate(image_names):
    print(f"{i}: {image_name}")

# Allow the user to select an image
selected_image_index = int(input("Enter the index of the image you want to select: "))

# Load the selected image
image_path = os.path.join(dataset_path, image_names[selected_image_index])
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is not None and not image.size == 0:

    # Define a function to load and pre-process an image
    def load_and_pre_process_image(image_path):
        # Load the image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Normalization: Ensure the image has consistent dimensions
        desired_height, desired_width = 160, 160
        image = cv2.resize(image, (desired_width, desired_height))

        

        # Pre-processing: Apply any desired pre-processing techniques
        blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

        return blurred_image

    # Pre-process the selected image
    preprocessed_image = load_and_pre_process_image(image_path)

    #This is a form of data visualization, as it allows the user to see and compare the two images. 
    # Display the original and pre-processed images, 
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap="gray")

    plt.subplot(1, 2, 2)
    plt.title("Pre-processed Image")
    plt.imshow(preprocessed_image, cmap="gray")

    plt.show()

else:
    print("Error: Unable to load or invalid image.")
