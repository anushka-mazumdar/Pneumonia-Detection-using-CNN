# Pneumonia Detection using CNN

## 🚀 Overview
This is an **Image Classification Web App** that utilizes a **Convolutional Neural Network (CNN)** to detect **Pneumonia** from chest X-ray images. The app consists of a **Flask backend** and an intuitive **HTML frontend**.

## 📁 Project Structure
```
📂 Project Root
│── app.py             # Flask backend for handling image uploads and predictions
│── image_class.ipynb  # Jupyter Notebook for model training and experimentation
│── ui.html            # Frontend HTML file for user interaction
```

## 🛠️ Features
- Upload a chest X-ray image via the web interface
- Send the image to the Flask backend for **Pneumonia classification**
- Receive and display the prediction result

## 🔧 Setup Instructions
### 1️⃣ Install Dependencies
Ensure you have **Python 3.7+** installed. Then, install the required libraries:
```bash
pip install flask tensorflow numpy pillow
```

### 2️⃣ Run the Flask Server
Start the Flask backend using:
```bash
python app.py
```
The server will be accessible at `http://127.0.0.1:5000`.

### 3️⃣ Open the Frontend
Simply open `ui.html` in your browser and upload a **chest X-ray image** for classification!

## 🖼️ Usage
1. Select a chest X-ray image.
2. Click the **Submit** button.
3. View the **Pneumonia detection result**.

## 🏗️ Future Enhancements
- Improve the CNN model for better accuracy.
- Add support for real-time image preprocessing.
- Deploy the app online for broader accessibility.

