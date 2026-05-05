# FastAPI Task Execution Service

A simple FastAPI-based web service demonstrating HTTP endpoints and modular Python application architecture.

## Description

This project showcases a modern Python web application built with FastAPI and Uvicorn, featuring:

- **main.py**: FastAPI application entry point with HTTP endpoints
- **utils.py**: Utility module containing the task execution function
- **requirements.txt**: Project dependencies

## Features

The application provides two HTTP endpoints:

- **GET `/`** - Root endpoint that returns server status
- **GET `/run-task`** - Endpoint that executes a task with a 3-second delay

## Project Structure

```
├── main.py          # FastAPI application and endpoint definitions
├── utils.py         # Utility functions (run_task)
├── requirements.txt # Project dependencies
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

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

## Learning Objectives

This project demonstrates:
- Building HTTP APIs with FastAPI
- Separation of concerns (API layer vs business logic)
- Module imports and code organization
- Using async-capable web frameworks
- Asynchronous server execution with Uvicorn
- REST API design principles
