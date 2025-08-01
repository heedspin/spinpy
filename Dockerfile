FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Set working directory
WORKDIR /spinpy

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a non-root user for security
RUN useradd -u 1000 -g 1000 --create-home --shell /bin/bash spinpy && chown -R spinpy:spinpy /spinpy
USER spinpy

# Command to run your application
CMD ["python", "main.py"]