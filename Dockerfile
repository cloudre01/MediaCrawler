FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
  chromium \
  chromium-driver \
  && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create directories for data and credentials
RUN mkdir -p /app/data /credentials

# Set environment variables
ENV PYTHONPATH=/app
ENV CHROME_PATH=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# The following env vars will be injected by Kubernetes
ENV TELEGRAM_BOT_TOKEN=""
ENV TELEGRAM_CHAT_ID=""
ENV GOOGLE_DRIVE_API_CREDENTIALS="/credentials/gdrive-credentials.json"

# Run the application
CMD ["python", "main.py"]
