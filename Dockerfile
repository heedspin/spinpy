FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a custom user with UID 1234 and GID 1234
RUN groupadd -g 1002 spinpygroup && \
    useradd -m -u 1002 -g spinpygroup -s /bin/bash spinpy

USER spinpy
WORKDIR /spinpy

CMD sh -c "echo 'Inside Container:' && echo 'User: $(whoami) UID: $(id -u) GID: $(id -g)'"

# Command to run your application
CMD ["python", "main.py"]