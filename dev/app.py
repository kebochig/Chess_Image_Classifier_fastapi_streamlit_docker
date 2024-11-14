# api_app.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image
import time
import tensorflow as tf
from tensorflow.keras.applications.mobilenet import preprocess_input
import uvicorn

# Initialize the FastAPI app
app = FastAPI()

# Load the trained MobileNet model
model = tf.keras.models.load_model('best_mobilenet_model.keras')

# Load class labels (Update these based on your dataset's class labels)
class_labels = {0: "Bishop", 1: "King", 2: "Knight", 3: "Pawn", 4: "Queen", 5: "Rook"}

# Helper Function: Preprocess Image for Inference
def preprocess_image(image: Image.Image):
    """Preprocesses an uploaded image for the MobileNet model."""
    img = image.resize((128, 128))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def make_prediction(image: Image.Image):
    """Makes a prediction on the input image and measures latency."""
    start_time = time.time()
    img_array = preprocess_image(image)
    predictions = model.predict(img_array)
    latency = time.time() - start_time

    predicted_class_index = np.argmax(predictions, axis=1)[0]
    confidence_score = np.max(predictions)

    # Convert TensorFlow types to native Python types
    predicted_label = class_labels[predicted_class_index]
    confidence_score = float(confidence_score)  # Convert float32 to float
    latency = float(latency)  # Convert float64 to float

    return predicted_label, confidence_score, latency

# Define the FastAPI route for prediction
@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file)
        predicted_label, confidence, latency = make_prediction(image)

        # Return the result as JSON
        return JSONResponse(content={
            "predicted_class": predicted_label,
            "confidence_score": round(confidence, 2),
            "latency": round(latency, 2)
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run('app:app', port=8000, host= '0.0.0.0')