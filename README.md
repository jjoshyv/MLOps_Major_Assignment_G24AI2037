## Automated MLOps Pipeline

This project implements a fully automated end-to-end MLOps workflow for training, testing, and deploying a machine learning model using modern DevOps practices.
The pipeline is built around the Olivetti Faces Dataset, with a focus on reproducibility, automation, and containerized deployment.

## Key Features

### 1. End-to-End ML Workflow

Loads and preprocesses the Olivetti Faces dataset

Trains an SVM classifier

Evaluates accuracy using a validation/test script

Saves the trained model as saved_models/savedmodel.pth

### 2. Fully Automated CI Pipeline (GitHub Actions)

Every push to docker_ci or PR to main triggers:

Environment setup

System dependency installation

Python package installation

Automated model training

Automated unit testing

Docker image build

Cleanup and summary logs

This guarantees reproducibility, consistent builds, and reliable testing.

### Dockerized Deployment

The application includes:

A Flask API for image upload and prediction

Containerized execution using Docker

Simple deploy/start instructions:

docker build -t mlops-olivetti-app .\
docker run -p 5000:5000 mlops-olivetti-app


The app exposes a web interface where users can upload face images and receive class predictions.

### Repository Structure

├── app.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                 # Flask API for face image prediction\
├── train.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;               # Model training script\
├── test.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                # Unit testing script\
├── saved_models/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          # Stores trained model (savedmodel.pth)\
├── Dockerfile&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;             # Containerization file\
├── requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       # Python dependencies\
├── screenshots/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          # UI images for documentation\
└── .github/workflows/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     # CI/CD pipeline configuration\


### MLOps Principles Implemented

Version control using Git & GitHub

Branching strategy:

&nbsp;&nbsp;&nbsp;main → stable release

&nbsp;&nbsp;&nbsp;dev → model development

&nbsp;&nbsp;&nbsp;docker_ci → CI/CD automation

Continuous Integration with automatic test + build

Containerization for consistent deployment

Reproducibility ensured through pinned dependencies and CI-based training

### Final Outcome

This project showcases a production-style MLOps workflow where:

&nbsp;&nbsp;&nbsp;Code commits trigger automatic training + testing

&nbsp;&nbsp;&nbsp;A Docker image is built reproducibly

&nbsp;&nbsp;&nbsp;The model is served through a simple but functional API

&nbsp;&nbsp;&nbsp;The entire lifecycle is automated and repeatable

This satisfies all assignment requirements for ML workflow automation, containerization, and CI/CD integration.

### To Clone the Repository
git clone https://github.com/jjoshyv/MLOps_Major_Assignment_G24AI2037.git



