MacroProject/
├── data/
│   └── raw/          
├── src/
│   ├── __init__.py       
│   ├── dataset.py         <-- index_dataset
│   ├── analysis.py        <-- plot_class_distribution
│   ├── model.py           <-- train_classifier
│   └── predictor.py       <-- predict_image
├── main.py                <-- File main (Training)
├── app.py                 <-- File run Tkinter
└── console_app.py         <-- File run Console
import os
import pandas as pd


def index_dataset(data_path):
    records = []

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset folder not found: {data_path}")

    for label in os.listdir(data_path):
        class_path = os.path.join(data_path, label)

        if os.path.isdir(class_path):
            for image_file in os.listdir(class_path):
                file_path = os.path.join(class_path, image_file)

                records.append({
                    "filepath": file_path,
                    "label": label
                })

    return pd.DataFrame(records)
import cv2
import matplotlib.pyplot as plt


def plot_class_distribution(df):
    print("\nClass distribution:")
    print(df["label"].value_counts())

    df["label"].value_counts().plot(kind="bar")
    plt.title("Class Distribution")
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def analyze_image_sizes(df):
    widths = []
    heights = []

    for path in df["filepath"]:
        image = cv2.imread(path)

        if image is not None:
            h, w = image.shape[:2]
            widths.append(w)
            heights.append(h)

    if widths:
        print("\nImage size analysis:")
        print(f"Average width: {sum(widths)/len(widths):.2f}")
        print(f"Average height: {sum(heights)/len(heights):.2f}")
        import cv2
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report


IMG_SIZE = 64


def preprocess_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return None

    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

    return image.flatten()


def train_classifier(df):
    X = []
    y = []

    for _, row in df.iterrows():
        processed = preprocess_image(row["filepath"])

        if processed is not None:
            X.append(processed)
            y.append(row["label"])

    X = np.array(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = SVC()

    print("\nTraining model...")
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\nClassification report:")
    print(classification_report(y_test, predictions))

    with open("macro_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("\nModel saved as macro_model.pkl")

    return model
import pickle
from src.model import preprocess_image


MODEL_PATH = "macro_model.pkl"


def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


def predict_image(image_path):
    model = load_model()

    processed = preprocess_image(image_path)

    if processed is None:
        return "Invalid image"

    prediction = model.predict([processed])

    return prediction[0]
from src.dataset import index_dataset
from src.analysis import plot_class_distribution
from src.analysis import analyze_image_sizes
from src.model import train_classifier


DATASET_PATH = "data/raw"


def main():
    print("Loading dataset...")

    df = index_dataset(DATASET_PATH)

    print(f"Found {len(df)} images")

    plot_class_distribution(df)

    analyze_image_sizes(df)

    train_classifier(df)


if __name__ == "__main__":
    main()
    from src.predictor import predict_image


def main():
    print("Macroinvertebrate Image Classifier")

    while True:
        image_path = input("\nEnter image path (or 'q' to quit): ")

        if image_path.lower() == "q":
            break

        result = predict_image(image_path)

        print("Prediction:", result)


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import filedialog

from src.predictor import predict_image


def choose_image():
    file_path = filedialog.askopenfilename()

    if file_path:
        prediction = predict_image(file_path)

        result_label.config(
            text=f"Prediction: {prediction}"
        )


root = tk.Tk()

root.title("Macroinvertebrate Classifier")
root.geometry("400x200")


title_label = tk.Label(
    root,
    text="Macroinvertebrate Classifier"
)

title_label.pack(pady=20)


upload_button = tk.Button(
    root,
    text="Choose Image",
    command=choose_image
)

upload_button.pack()


result_label = tk.Label(
    root,
    text=""
)

result_label.pack(pady=20)


root.mainloop()
