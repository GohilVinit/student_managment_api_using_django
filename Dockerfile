# Use the official Python image as a parent image
FROM python:3.12-slim

# Install PostgreSQL development libraries and build tools (including gcc)
RUN apt-get update && apt-get install -y libpq-dev gcc

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
