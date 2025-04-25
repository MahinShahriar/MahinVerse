FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libpq-dev \
    && apt-get clean

# Install Node.js (for Tailwind)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Tailwind build (assuming theme app has package.json)

RUN npm install && python manage.py tailwind install

# Collect static and migrate

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate


CMD gunicorn your_project.wsgi:application --bind 0.0.0.0:8000
