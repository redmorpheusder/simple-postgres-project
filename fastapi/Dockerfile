# Use a slim Python image as the base
FROM python:3.11-slim

# Set environment variables to prevent Python from writing pyc files and to buffer outputs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install dependencies directly into the container without a virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Railway will bind to dynamically
EXPOSE ${PORT}

# Start the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
