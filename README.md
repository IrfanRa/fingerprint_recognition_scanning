# Secure Attendance System based on Blockchain Technology, Fingerprint Recognition Scanning

=============================================================================

Develop a Fingerprint recognition biometric authentication attendance system based on Blockchain technology that can accurately identify individuals using fingerprint scanning recognition.
The input variables/features for this problem:
• Fingerprint image of the output variable/feature for this problem:
• True/False (indicating whether the fingerprint image matches a known individual) biometric authentication dataset (fingerprint scanning).

## Here's the project structure

biometric_authentication_project/
├── data/
│   ├── fingerprint_dataset/
│   │   ├── np_data/
│   │   │   ├── img_real.npy
│   │   │   ├── img_train.npy
│   │   │   ├── label_real.npy
│   │   │   └── label_train.npy
│   │   ├── real_data/
│   │   │   ├── 00001.bmp
│   │   │   ├── 00002.bmp
│   │   │   └── ...
│   │   └── train_data/
│   │       ├── 00000_00.bmp
│   │       ├── 00000_01.bmp
│   │       └── ...
├── database/
│   ├── biometric_data.db
├── code/
│   ├── task1_database_integration.py
│   ├── task2_data_analysis_preprocessing.py
│   ├── task3_feature_extraction.py
├── requirements.txt
└── README.md

## Task No.1

    1.1. Develop a code regarding export/import and SQLite database integration procedures with Python.
    1.2. Load the dataset from the SQLite database on any Python platform.
    1.3. Required libraries:
            sqlite3
            numpy as np

### Task No. 2

    2.1. Develop the code regarding normalizing and pre-processing.
    normalizing: a basic form of normalization by resizing the images to a consistent size.
    pre-processing: a pre-processing technique known as "Gaussian blur" is applied to the loaded image.
    2.2. You must also show data visualization procedures in the code platform.
    a form of data visualization, as it allows the user to see and compare the two images.Display the original and pre-processed images.
    2.3. Required libraries:
            cv2
            numpy as np
            matplotlib.pyplot as plt
            os

### Task No.3

    3.1. You will have to mention the source and reason for choosing selected attendance features/attributes of the dataset:
    Source of Features: The features for this dataset are extracted from fingerprint images provided by the FVC2000 dataset.
    Reasons for Selection:
        3.1.1. Thresholding: Thresholding is applied to segment the fingerprint image into foreground (ridge patterns) and background.
                This segmentation process is essential for isolating the fingerprints unique features and removing unwanted noise.
        3.1.2. Edge Detection: Detecting edges in the fingerprint images is crucial because it helps identify the ridge structures.
                These ridges contain valuable information for fingerprint matching, and edge detection aids in their extraction.
    3.2. Required libraries:
            cv2
            numpy as np
    3.3. Source Citation:
            Fingerprint Dataset FVC2000_DB4_B
            <https://www.kaggle.com/datasets/peace1019/fingerprint-dataset-for-fvc2000-db4-b>
