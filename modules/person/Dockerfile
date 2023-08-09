# Base Image
FROM python:3.8-alpine

# Set the working directory
WORKDIR /app

# Install gcc, musl-dev, linux-headers, geos, libc-dev, postgresql-dev, build-base, and g++
RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev build-base g++

# Copy requirements.txt to the container
COPY requirements.txt requirements.txt

# Install Python packages
RUN pip install -r requirements.txt

# Copy rest of the application to the container
COPY . .

# Set environment variables
ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONPATH=/app

# Expose port 5000
EXPOSE 5000

# Default command to run
CMD ["flask", "run", "--host", "0.0.0.0"]
