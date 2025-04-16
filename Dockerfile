# Use Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files (including requirements.txt) to /app inside the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "app.py"]

EXPOSE 5000
