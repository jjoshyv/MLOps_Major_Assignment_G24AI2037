FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

# Install minimal system build deps (removed libatlas-base-dev)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      gcc \
      g++ \
      gfortran \
      pkg-config \
      libopenblas-dev \
      libblas-dev \
      liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Upgrade pip/tools
RUN python -m pip install --upgrade pip setuptools wheel

# Install numpy & scipy first (prefer binary wheels)
RUN pip install --no-cache-dir numpy scipy

# Install remaining Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
