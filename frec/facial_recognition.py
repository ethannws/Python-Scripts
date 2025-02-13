FROM nvidia/cuda:11.2.2-cudnn8-runtime-ubuntu20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install opencv-python dlib face_recognition scikit-learn

# Copy the facial recognition script
COPY facial_recognition.py /app/facial_recognition.py

# Set the working directory
WORKDIR /app

# Run the facial recognition script
CMD ["python3", "facial_recognition.py"]
