# Use the official Python 3.9 image as the base
FROM python:3.11.4-slim

# Set the working directory in the container
WORKDIR /src

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends g++ python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port for the FastAPI application
EXPOSE $PORT

WORKDIR /src/app

# Start the FastAPI application using uvicorn
CMD exec uvicorn --port $PORT --host 0.0.0.0 main:app --reload
