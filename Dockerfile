FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

ARG SPINPY_UID=1001
ARG UBUNTU_GROUP=1000
RUN useradd -m -u ${SPINPY_UID} -g ${UBUNTU_GROUP} -s /bin/bash spinpy

USER spinpy
WORKDIR /spinpy

# CMD sh -c "echo 'Inside Container:' && echo 'User: $(whoami) UID: $(id -u) GID: $(id -g)'"

# Command to run your application
CMD ["python", "main.py"]