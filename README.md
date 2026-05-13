
Macroinvertebrate Image Analysis System 🔍🐜

Project Goal

This application is designed to analyze macroinvertebrate image data, generate Exploratory Data Analysis (EDA) outputs, train a baseline machine learning classifier, and provide a deployed interface (Tkinter or Console) for image prediction. 

🌟 Main Features

- Dataset Indexing: Automatically scans directory structures to catalog image metadata, including labels, dimensions, and color channels.
  
- Class Distribution Analysis: Visualizes the number of images per category to identify potential data imbalances .
  
- Image Size Analysis: Calculates and plots the distribution of image widths and heights across the dataset .
  
- Baseline Classification: Trains a Random Forest (or SVM) model to recognize different species using a consistent preprocessing pipeline .
  
- Deployed Prediction Interface: Provides a user-friendly GUI (Tkinter) or a menu-driven Console application to predict species from new images .
  
🛠 Python Packages UsedThe system utilizes several specialized libraries for data science and computer vision :

Pandas: Used to store indexed image records and support tabular analysis.

OpenCV: Handles image reading, resizing, and grayscale preprocessing.

Scikit-learn: Powers the train/test split and the baseline classification model .

Matplotlib & Seaborn: Generates EDA charts and model evaluation visuals like the Confusion Matrix.

Joblib: Manages the saving and loading of trained model artifacts.  Tkinter: Provides the desktop interface for Stage 3 deployment.

📂 Folder StructureThe project follows a modular Object-Oriented design to ensure maintainability and clear separation of concerns :

macro_project/
├── data/raw/             # Raw images organized by class folders

├── outputs/              # Saved EDA charts and trained models (.joblib)

├── src/
│   ├── models/           # Data classes (e.g., ImageRecord)
│   ├── services/         # Logic for Indexing, EDA, Preprocessing, and Training
│   ├── main.py           # Entry point for Stage 1 & 2 workflows
│   ├── app.py            # Tkinter GUI application (Stage 3)
│   └── console_app.py    # Menu-driven Console application (Stage 3)
└── requirements.txt      # List of required dependencies
🚀 How to Run

1. Install Dependencies
   
Ensure you have Python installed, then run the following command to install required libraries:
pip install pandas numpy opencv-python matplotlib seaborn scikit-learn Pillow joblib

2. Prepare Data
   
Place your image dataset inside the data/raw/ directory. Each subfolder should be named after the species (e.g., data/raw/mayfly/image1.jpg).

3. Execution
Run Stage 1 & 2 (EDA & Training):

python -m src.main

Run Stage 3 (Deployment):

For the Desktop GUI: python -m src.app   

For the Console Menu: python -m src.console_app

🧪 Testing Evidence

The application includes error handling and has been verified through manual testing scenarios :  

Graceful handling of missing dataset folders or model files.

Validation for invalid image paths or unsupported file types.

Verification of end-to-end prediction flow with valid inputs.

👤 Authors
Tuan Nam Ngo


Team: Database Group 3
