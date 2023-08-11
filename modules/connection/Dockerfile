# Base Image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y gcc g++ libpq-dev libgeos-c1v5 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements.txt to the container
COPY requirements.txt requirements.txt

# Install Python packages
RUN pip install -r requirements.txt

# For production-ready setup, install Gunicorn
RUN pip install gunicorn

# Copy rest of the application to the container
COPY . .

# Set environment variables
ENV FLASK_APP=wsgi.py
ENV PYTHONPATH=/app

# Expose port 5000
EXPOSE 5000

# Use Gunicorn as the entry point to serve the app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
