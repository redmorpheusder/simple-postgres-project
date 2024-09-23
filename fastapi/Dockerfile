<<<<<<< HEAD
# Use the official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port (Railway sets this automatically)
EXPOSE ${PORT}

# Command to run your application
CMD ["python", "app.py"]
=======
# Используем Python image
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт (уже не указываем конкретное значение, он будет динамическим через ENV)
EXPOSE ${PORT}
>>>>>>> e280e51107ab05c91aa9cc8e5e33a8b773391049
