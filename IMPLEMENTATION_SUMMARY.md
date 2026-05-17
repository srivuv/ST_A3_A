## Project Title & Group Members

- U3322254
- U3283098
- U3318286

## Project Goal

Perform EDA on macroinvertebrate dataset, train model to identify insects using dataset, give user a GUI to use trained model to identify insect species.

## System Design Overview

Project structured as modular Python application with seperated dataset indexing, EDA, image preprocessing, classification, and user interface. Seperation was done using Python classes and modules. This mdae project easier to build, test, maintain, and document. Stage 1 workflow generated charts and summary outputs from dataset, Stage 2 workflow trains baseline classifier on preprocessed grayscale images. Deployed application loads trained model, allows user to provide image and view predicted macroinvertebrate class.

## Class & Module Overview

- ClassifierService
    - Train, evaluate, and persist the baseline classification model.
    
- DatasetIndexer
    - Scan the dataset folder and build a tabular image index.

- EDAService
    - Generate and save EDA outputs for the indexed image dataset.

- ImagePreprocessor
    - Convert raw images into model-ready numeric features.

- WorkflowService
    - Coordinate the shared workflow used by batch, GUI, and console entry points.

- ImageRecord
    - Store the core metadata for one indexed macroinvertebrate image.

- Config
    - This configuration module helps store paths and reusable settings in one easy-to-access place; improving readability, avoiding hard-coded values and allowing project-wide changes seamlessly and efficiently.

## Python Packages Used & Why

- Pandas: Used to store indexed image records and support tabular analysis.

- OpenCV: Handles image reading, resizing, and grayscale preprocessing.

- Scikit-learn: Powers the train/test split and the baseline classification model .

- Matplotlib & Seaborn: Generates EDA charts and model evaluation visuals like the Confusion Matrix.

- Joblib: Manages the saving and loading of trained model artifacts.  Tkinter: Provides the desktop interface for Stage 3 deployment.

## Key Features Implemented

Key features include EDA on provided dataset, training model on provided dataset, and providing user with easy-to-use GUI to predict class of object within an image.

## Testing Summary 

Testing went successfully. Full project works as expected. Even when model file is missing, project trains model on-the-spot and uses model as normal.

## Screenshots

![Screenshot 1](Screenshot1.png)

## Reused or Adapted Code Acknowledgement

Almost all code in project is originally derived from "Assignment 3 Full Guidance and Coding Examples.pdf" from Software Technology (4483 SEM-1 2026 BRUCE ON-CAMPUS) module "Assignment 3 Docs".

## Work Division Summary

u3283098 worked on GUI and README.md.

u3318286 worked on main.py and workflow service.

u3322254 worked on modules and classes used by workflow service, made GUI run from main.py, fixed code formatting errors, wrote MANUAL_TESTING.md and IMPLEMENTATION_SUMMARY.md.