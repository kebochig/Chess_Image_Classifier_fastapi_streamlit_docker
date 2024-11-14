# Chess Piece Classification API and Interface

This project provides an end-to-end solution for Chess Piece classification using a MobileNet-based CNN model with FastAPI and Streamlit. The project allows users to upload images, get classification results, and view performance metrics.

## Features
- **FastAPI** for serving the image classification model via a REST API.
- **Streamlit** for an intuitive user interface that allows image uploads and visualization of results.
- **Docker** for easy deployment and containerization.
- **Real-time performance metrics** displayed on the Streamlit interface.

---

## Setup and Running the Project

### Prerequisites
- Docker and Docker Compose installed on your machine.
- Python 3.9+ (if running locally without Docker).

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/Image-Classification-Project.git
cd Chess_Image_Classifier/dev

### Step 2: Build and Run the Docker Containers
Use Docker Compose to build and run both the FastAPI and Streamlit containers.

```bash
docker-compose up --build

- The FastAPI app will be available at http://localhost:8000.
- The Streamlit app will be accessible at http://localhost:8501.

### Step 3: Access the Interfaces

FastAPI: You can test the API endpoints using a tool like Postman or directly in your browser at http://localhost:8000/docs.
Streamlit: Visit http://localhost:8501 to upload images and view classification results.


Running Locally (Without Docker)
Step 1: Install Dependencies
Create a virtual environment and install the dependencies listed in requirements.txt and requirements_streamlit.txt.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements_streamlit.txt

Step 2: Run the FastAPI App
```bash
uvicorn app.api_app:app --host 0.0.0.0 --port 8000

Step 3: Run the Streamlit App
```bash
streamlit run app/streamlit_app.py


Troubleshooting

Common Issues and Fixes
1. Port Already in Use

    If you get an error indicating that a port is already in use, try stopping the process using that port or change the port in the docker-compose.yml file.

2. Memory Issues During Model Loading

    Ensure your system has enough memory to load the MobileNet model. If not, consider using a machine with higher RAM or a smaller model.
    
3. Docker Build Failures

    Double-check that all required files are in the correct locations and that requirements.txt lists all dependencies.

4. Model Prediction Errors

    Ensure the image you upload is in a compatible format. If errors persist, try debugging using print statements in model_utils.py.