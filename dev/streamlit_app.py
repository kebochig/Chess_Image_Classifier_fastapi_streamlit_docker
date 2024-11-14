# streamlit_app.py

import streamlit as st
import requests
from PIL import Image
import time

# FastAPI endpoint
# API_URL = "http://127.0.0.1:8000/predict/"
API_URL = "http://fastapi:8000/predict/"


# Streamlit Interface
st.title("Chessman Image Classification ♞")
st.write("Upload an image of a chess piece to classify it into one of the following categories: Bishop, King, Knight, Pawn, Queen, or Rook.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Classifying...")

    # Measure the start time for performance tracking
    start_time = time.time()

    # Send the image to the FastAPI server
    try:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(API_URL, files=files)
        result = response.json()

        if response.status_code == 200:
            # Measure the end time and calculate total time
            end_time = time.time()
            total_latency = result["latency"]
            throughput = 1 / total_latency if total_latency > 0 else 0

            # Display results
            # st.write(f"**Predicted Class**: {result['predicted_class']}")
            # st.write(f"**Confidence Score**: {result['confidence_score']}")
            # st.write(f"**Latency**: {total_latency:.2f} seconds")
            # st.write(f"**Throughput**: {throughput:.2f} images per second")

            # Display additional performance metrics
            st.metric(label="Predicted Class", value=f"{result['predicted_class']}")
            st.metric(label="Confidence Score", value=f"{result['confidence_score']:.2f} %")
            st.metric(label="Latency", value=f"{total_latency:.2f} s")
            st.metric(label="Throughput", value=f"{throughput:.2f} images/s")
        else:
            st.error("Error in classification. Please try again.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
