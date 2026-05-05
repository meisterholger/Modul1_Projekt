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

