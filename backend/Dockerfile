# backend/Dockerfile

FROM python:3.12-slim

# Set the working directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    ca-certificates \
    openssl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /code/

# Copy and set permissions for entrypoint.sh
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint and default command
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
