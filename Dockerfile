# Use official Python image
FROM python:3.11-slim

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /main

# Install dependencies
COPY requirements.txt /main/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /main/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run the app
CMD ["gunicorn", "urlshortner.wsgi:application", "--bind", "0.0.0.0:8000"]
