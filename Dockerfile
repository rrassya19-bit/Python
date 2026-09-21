FROM python:3.13-slim

WORKDIR /app

# Install dependencies yang dibutuhkan sistem
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy konfigurasi package
COPY pyproject.toml requirements.txt dev-requirements.txt ./

# Install dependensi Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt -r dev-requirements.txt

# Copy seluruh kode sumber
COPY . .

# Default command menjalankan pytest
CMD ["pytest"]
