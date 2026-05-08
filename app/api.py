"""
FastAPI application module.

This module creates and configures the FastAPI application instance,
defining endpoints:
- GET /: Root endpoint that returns server status
- POST /run-task: Endpoint that executes a task with provided type and data
"""

from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from app.utils import run_task


class TaskRequest(BaseModel):
    """Request model for task execution endpoint."""

    task_type: str
    task_data: dict


class TaskResponse(BaseModel):
    """Response model for task execution endpoint."""

    task: str
    status: str
    message: Any
    result: dict | None


app = FastAPI()


@app.get("/")
def root_endpoint() -> dict[str, str]:
    """
    Endpoint for the root URL that returns server status.

    Returns:
        dict: A message confirming the server has started successfully.
    """
    return {"message": "Server started successfully!"}


@app.post("/run-task", response_model=TaskResponse)
def run_task_endpoint(request: TaskRequest) -> dict:
    """
    Endpoint to execute a task based on task type and data.

    Args:
        request (TaskRequest): Request containing task_type and task_data.

    Returns:
        TaskResponse: Task execution result with status and data.
    """
    response = run_task(request.task_type, request.task_data)
    return response
