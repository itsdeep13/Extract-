# Base Image
FROM python:3.11-slim

# System Dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    ffmpeg \
    aria2 \
    build-essential \
    python3-dev \
    libopenblas-dev \
    liblapack-dev \
    gfortran \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    cargo \
    rustc \
    ninja-build \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and core build tools
RUN pip install --upgrade pip setuptools wheel meson

# Copy requirements
COPY requirements.txt /requirements.txt

# Pre-install pandas to avoid build isolation failure
RUN pip install "pandas==2.2.2" --no-build-isolation --no-cache-dir

# Install remaining dependencies
RUN pip install -r /requirements.txt --no-cache-dir

# App directory
RUN mkdir /app
WORKDIR /app

# Copy startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Start command
CMD ["/bin/bash", "/start.sh"]
