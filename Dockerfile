# Use an optimized Python image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt /app/

# Install dependencies (use pip cache for faster builds)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

# Expose port 5000
EXPOSE 5000

# Run the application using Gunicorn for better performance
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

