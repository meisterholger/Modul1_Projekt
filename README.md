# FastAPI Task Execution Service

A simple FastAPI-based web service demonstrating HTTP endpoints and modular Python application architecture.

## Description

This project showcases a modern Python web application built with FastAPI and Uvicorn, featuring:

- **app/**: Application package with FastAPI endpoints and utilities
- **main.py**: Application entry point for Uvicorn server
- **tests/**: Comprehensive test suite with pytest
- **pyproject.toml**: Modern Python project configuration

## Features

The application provides two HTTP endpoints:

- **GET `/`** - Root endpoint that returns server status
- **GET `/run-task`** - Endpoint that executes a task with a 3-second delay

## Project Structure

```
Modul1_Projekt/
├── app/
│   ├── __init__.py      # Package definition
│   ├── api.py           # FastAPI application and endpoints
│   └── utils.py         # Utility functions (run_task)
├── tests/
│   ├── __init__.py      # Test package
│   ├── test_api.py      # Tests for endpoints
│   └── test_utils.py    # Tests for utilities
├── main.py              # Entry point (Uvicorn server startup)
├── pyproject.toml       # Project metadata and dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Installation

1. Clone or navigate to the project directory
2. Install the package in development mode:

```bash
pip install -e ".[dev]"
```

This installs the project with all development dependencies including pytest.

## Running the Application

Start the development server:

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Documentation

FastAPI provides interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Docker Deployment

### Build Docker Image

Create a `Dockerfile` in the project root:

```dockerfile
FROM python:3.13.2
LABEL maintainer="Holger Meister"

COPY . /app
WORKDIR /app

RUN pip install -e .

CMD ["python", "main.py"]
```

Build the image:

```bash
docker build -t api-service .
```

### Run Docker Container

Run the container with port mapping:

```bash
docker run -d -p 8000:8000 api-service
```

The API will be available at `http://localhost:8000`

**Note:** The application is configured to listen on `0.0.0.0:8000` to be accessible from outside the container.

### Container Logs

View container logs:

```bash
docker logs <container_id>
```

Stop the container:

```bash
docker stop <container_id>
```

## Kubernetes Deployment

### Prerequisites

- Kubernetes cluster (e.g., Minikube, K3s, or cloud provider)
- `kubectl` command-line tool installed
- Docker image pushed to a registry (e.g., Docker Hub)

### Project Structure

Kubernetes manifests are located in the `kubernetes/` directory:

```
kubernetes/
├── namespace.yaml      # Namespace for application isolation
├── service.yaml        # LoadBalancer service for external access
└── deployment.yaml     # Deployment with 2 replicas, health checks, and resource limits
```

### Deploy to Kubernetes

1. Create the namespace, deployment, and service:

```bash
# Apply all manifests in order
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

# Or apply all at once
kubectl apply -f kubernetes/
```

2. Verify deployment:

```bash
# Check all resources in the namespace
kubectl get all -n apiservice

# Check deployment status
kubectl get deployment -n apiservice

# Check pod logs
kubectl logs -n apiservice -l app=api-service -f
```

### Configuration Details

**Deployment Configuration:**
- **Replicas**: 2 for high availability
- **Resource Requests**: 64Mi memory, 100m CPU
- **Resource Limits**: 128Mi memory, 500m CPU
- **Liveness Probe**: Checks container health every 10 seconds
- **Readiness Probe**: Checks pod readiness every 5 seconds

**Service Configuration:**
- **Type**: LoadBalancer (for external access)
- **Port**: 8000 (exposed externally)
- **Target Port**: 8000 (container port)

### Access the Application

Once deployed, get the external IP:

```bash
kubectl get service -n apiservice

# URL will be available at: http://<EXTERNAL-IP>:8000
# Swagger UI: http://<EXTERNAL-IP>:8000/docs
```

### Troubleshooting

Check pod status:

```bash
kubectl describe pod -n apiservice -l app=api-service
```

View application logs:

```bash
kubectl logs -n apiservice -l app=api-service --tail=50
```

Delete deployment:

```bash
kubectl delete namespace apiservice
```

## Testing

Run the test suite:

```bash
pytest tests/ -v
```

Run specific tests:

```bash
pytest tests/test_api.py -v      # Test endpoints
pytest tests/test_utils.py -v    # Test utilities
```

## Endpoints

### Root Endpoint

```
GET /
```

Returns:
```json
{"message": "Server started successfully!"}
```

### Task Execution Endpoint

```
GET /run-task
```

Executes the task function with a 3-second delay.

Returns:
```json
{"message": "Task completed successfully"}
```

## Dependencies

### Production
- **fastapi** - Web framework
- **uvicorn** - ASGI server

### Development
- **pytest** - Testing framework
- **httpx** - HTTP client for testing

See `pyproject.toml` for version specifications.

## Learning Objectives

This project demonstrates:
- Building HTTP APIs with FastAPI
- Separation of concerns (API layer vs business logic)
- Package organization and module imports
- Using async-capable web frameworks
- Asynchronous server execution with Uvicorn
- REST API design principles
- Test-driven development with pytest
- Modern Python project structure with pyproject.toml

