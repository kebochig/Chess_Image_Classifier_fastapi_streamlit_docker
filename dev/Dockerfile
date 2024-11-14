# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the FastAPI app using Uvicorn
# CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000"] CMD ["uvicorn", "app:app", "--reload"]
CMD ["fastapi", "run", "app.py"]
