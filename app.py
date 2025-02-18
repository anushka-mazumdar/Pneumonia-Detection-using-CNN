import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable frontend communication

# Model file path
MODEL_PATH = 'best_model.h5'

# Ensure model exists before loading
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file '{MODEL_PATH}' not found. Ensure it's in the correct directory.")

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Debugging: Print model summary
print("Model Loaded Successfully!")
print(model.summary())  # Check the last layer (how many output classes?)

# Define class labels (update based on your model's training)
CLASS_LABELS = {0: "No Pneumonia Detected", 1: "Pneumonia Detected"}

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    """Check if the uploaded file has a valid extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['POST'])
def predict():
    """Handles image classification requests."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Allowed types: png, jpg, jpeg'}), 400

    try:
        # Read and preprocess the image
        image = Image.open(io.BytesIO(file.read()))
        image = image.convert('RGB')  # Ensures 3 color channels (RGB)
        image = image.resize((150, 150))  # Resize to match model input size
        image = np.array(image) / 255.0  # Normalize pixel values (0-1)
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Make prediction
        predictions = model.predict(image)
        predicted_class = np.argmax(predictions[0])  # Get class with highest probability
        predicted_label = CLASS_LABELS.get(predicted_class, "Unknown")  # Get label

        # Debugging: Print predictions
        print(f"Raw Model Output: {predictions}")  # Show probabilities of all classes
        print(f"Predicted Class: {predicted_class}")  # Show final class
        print(f"Predicted Label: {predicted_label}")  # Show final label

        return jsonify({'prediction': predicted_label})

    except Exception as e:
        return jsonify({'error': f'Processing error: {str(e)}'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
