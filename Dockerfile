FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Set working directory
WORKDIR /spinpy

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# host user / ubuntu user's UID/GID and pass as build args
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd spinpy && useradd -g spinpy -m -s /bin/bash spinpy

USER spinpy

# Command to run your application
CMD ["python", "main.py"]