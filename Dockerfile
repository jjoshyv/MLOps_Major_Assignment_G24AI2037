# Use a lightweight Python base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Command to run the Flask API
CMD ["python", "app.py"]
