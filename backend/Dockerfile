FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install Flask
RUN pip install Flask

# Copy entire project into container
COPY . /app

# Expose Flask default port
EXPOSE 5000

# Run the application
CMD ["python", "run.py"]
