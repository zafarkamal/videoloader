# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set metadata as labels
LABEL maintainer="Your Name <your.email@example.com>"
LABEL version="1.0"
LABEL description="This is a Docker image for the githubConnect.py script"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the requests package directly
RUN pip install --no-cache-dir -r requirements.txt

# Run the script when the container launches
CMD ["python", "githubConnect.py"]
