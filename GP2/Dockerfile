FROM python:3.9
MAINTAINER Wesam Aljuraish "wsam76@hotmail.com"

# Install system dependencies
RUN apt-get update -y \
    && apt-get install -y python3-pip python3-dev build-essential \
    && apt-get install -y libgl1-mesa-glx libsm6 libxrender1 libfontconfig1

# Set the working directory in the container
WORKDIR /GP2

# Copy the application requirements file into the container
COPY requirements.txt requirements.txt

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Specify the command to run on container start
CMD ["python", "app.py"]
