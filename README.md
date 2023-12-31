# Secure Attendance System based on Blockchain Technology, Fingerprint Recognition Scanning
Develop a Fingerprint recognition biometric authentication attendance system based on Blockchain technology, 
that can accurately identify individuals using fingerprint scanning recognition.
<br>
The input variables/features for this problem:<br>
    •  Fingerprint image of the output variable/feature for this problem. 
<br>
    •  True/False (indicating whether the fingerprint image matches a known individual) biometric authentication dataset (fingerprint scanning).

### Task No.1
    1.1. Develop a code regarding export/import and SQLite database integration procedures with Python.
    1.2. Load the dataset from the SQLite database on any Python platform.
    1.3. Required libraries:
            sqlite3
            numpy as np
            
### Task No. 2
    2.1. Develop the code regarding normalizing and pre-processing.
            normalizing: a basic form of normalization by resizing the images to a consistent size.
            pre-processing: a pre-processing technique known as "Gaussian blur" is applied to the loaded image.
    2.2. show data visualization procedures in the code platform.
            data visualization, as it allows the user to see and compare the two images. Display the original and pre-processed images.
    2.3. Required libraries:
            cv2
            numpy as np
            matplotlib.pyplot as plt
            os

### Task No.3
    3.1. You will have to mention the source and reason for choosing selected attendance features/attributes of the dataset:
            Source of Features: The features for this dataset are extracted from fingerprint images provided by the FVC2000 dataset.
         Reasons for Selection:
            3.1.1. Thresholding: Thresholding is applied to segment the fingerprint image into foreground and background.
                    This segmentation process is essential for isolating the fingerprint's unique features and removing unwanted noise.
            3.1.2. Edge Detection: Detecting edges in the fingerprint images is crucial because it helps identify the ridge structures.
                    These ridges contain valuable information for fingerprint matching and edge detection aids in their extraction.
    3.2. Required libraries:
            cv2
            numpy as np
    3.3. Source Citation:
            Fingerprint Dataset FVC2000_DB4_B
            https://www.kaggle.com/datasets/peace1019/fingerprint-dataset-for-fvc2000-db4-b
