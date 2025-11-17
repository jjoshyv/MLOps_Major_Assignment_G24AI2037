## Automated MLOps Pipeline

This project implements an end-to-end MLOps workflow involving dataset loading, model training, evaluation, and API deployment.
It follows the key principles of Reproducibility, Automation, Version Control, and Containerized Deployment.

The model used in this pipeline is a Support Vector Machine (SVM) trained on the Olivetti Faces dataset, a classic face-recognition dataset containing 400 grayscale facial images.

### 1. Project Overview

The goal of this assignment is to design and execute an automated MLOps pipeline that includes:

Data loading & preprocessing

Model training and evaluation

Saving trained models

Testing the model on unseen data

Deploying the ML model using a Flask API

Managing the pipeline using:

Virtual environments

Git for version control

Docker for reproducible execution

This project demonstrates how Machine Learning workflows can be automated and packaged for deployment.

### 2. Project Structure
MLOps_Major_Assignment/\
│── app.py&nbsp;&nbsp;&nbsp;           # Flask API for model prediction\
│── train.py&nbsp;&nbsp;&nbsp;           # Training script (model creation + saving)\
│── test.py&nbsp;&nbsp;&nbsp;             # Script to test trained model accuracy\
│── saved_models&nbsp;&nbsp;&nbsp;    # Folder generated after training\
│── requirements.txt&nbsp;&nbsp;&nbsp;     # Python dependencies\
│── venv/&nbsp;&nbsp;&nbsp;                # Virtual environment (ignored in Git)\
└── README.md&nbsp;&nbsp;&nbsp;           # Project documentation\


### 3. Dataset Used
Olivetti Faces Dataset

400 images

64×64 grayscale

40 individuals (10 images each)

Loaded directly using:

from sklearn.datasets import fetch_olivetti_faces

This dataset is included in sklearn.datasets, so no external download is required.

### 4. How to Run the Project
Step 1 — Clone the Repository\
git clone https://github.com/jjoshyv/MLOps_Major_Assignment_G24AI2037.git\
cd MLOps_Major_Assignment_G24AI2037\

Step 2 — Create & Activate a Virtual Environment\
python3 -m venv venv\
source venv/bin/activate\

Step 3 — Install Dependencies\
pip install -r requirements.txt\

Step 4 — Train the Model\
This loads the dataset, trains an SVM classifier, and saves it into saved_models/.\
python3 train.py\

Step 5 — Test the Model\
python3 test.py\

Step 6 — Run the Flask API\
Start the API server:\
python3 app.py\

### 5. Docker Support
To build the container:\
docker build -t mlops-pipeline .\

Run the container:\
docker run -p 5000:5000 mlops-pipeline

This ensures the ML pipeline is fully reproducible and portable.

### 6. Requirements

All dependencies are included in requirements.txt.\
Key libraries:

scikit-learn

numpy

flask

pillow

gunicorn (for production)

### 7. Key Features

Fully automated ML training + testing

Reproducible through Docker

Clean API for inference

Model persistence for reuse

Version-controlled workflow (GitHub)

Virtual environment isolation

Modular Python scripts