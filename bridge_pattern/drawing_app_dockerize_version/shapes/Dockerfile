FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Generate gRPC code (for shapes and drawing_apis services)
RUN python -m grpc_tools.protoc --proto_path=./proto --python_out=./proto --grpc_python_out=./proto drawing.proto

# Set the entrypoint
CMD ["python", "shapes_service.py"]