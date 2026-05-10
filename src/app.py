import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import joblib
from PIL import Image, ImageTk

class MacroApp(tk.Tk):

    def __init__(self, preprocessor, model_path: Path) -> None:
        super().__init__()
        self.title("Macroinvertebrate Image Analysis System")
        self.geometry("900x700")
        
        self.preprocessor = preprocessor
        self.model = joblib.load(model_path)
        self.selected_file = None

        if not model_path.exists():
            messagebox.showerror("Error", f"Cannot find file model at: {model_path}")
            self.destroy()
            return


        self.title_label = tk.Label(self, text="Image analysis system", font=("Arial", 18, "bold"))
        self.title_label.pack(pady=20)

        self.image_label = tk.Label(self, text="not picked", bg="gray90", width=50, height=20)
        self.image_label.pack(pady=10)

        self.result_label = tk.Label(self, text="Result will be shown here", font=("Arial", 14), fg="blue")
        self.result_label.pack(pady=20)

  
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Choose image", command=self.choose_image, width=15).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Guess", command=self.predict_image, width=15, bg="lightgreen").pack(side=tk.LEFT, padx=10)

    def choose_image(self) -> None:

        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
        )
        if not file_path:
            return

        self.selected_file = file_path
        try:
            image = Image.open(file_path)
            image.thumbnail((400, 400)) 
            photo = ImageTk.PhotoImage(image)
            
            self.image_label.configure(image=photo, text="")
            self.image_label.image = photo
        except Exception as e:
            messagebox.showerror("Lỗi", f"Cannot show image: {e}")

    def predict_image(self) -> None:
    
        if not self.selected_file:
            messagebox.showwarning("Announcement", "Please choose an image first!")
            return

        try:
         
            features = self.preprocessor.transform(self.selected_file).reshape(1, -1)
            
      
            prediction = self.model.predict(features)[0]
            
        
            if hasattr(self.model, "predict_proba"):
                probability = self.model.predict_proba(features).max()
                text = f"Result: {prediction}\nReliability: {probability:.2%}"
            else:
                text = f"Result: {prediction}"
            
            self.result_label.configure(text=text, fg="darkgreen")

        except Exception as e:

            messagebox.showerror("Prediction error", f"An error occurred while processing the image:\n{str(e)}")