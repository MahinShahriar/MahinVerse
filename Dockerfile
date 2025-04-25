# Use official Python image
FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the entire app
COPY . .

# Build Tailwind CSS
WORKDIR /app/theme
RUN npm install

# Back to Django app root
WORKDIR /app

# Collect static files (optional if you want static to serve via WhiteNoise or CDN)
RUN python manage.py collectstatic --noinput || true

# Expose port and start Gunicorn
CMD gunicorn MahinVerse.wsgi:application --bind 0.0.0.0:8000
