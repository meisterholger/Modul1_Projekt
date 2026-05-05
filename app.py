"""
FastAPI application module.
This module creates and configures the FastAPI application instance,
defining two endpoints:
- GET /: Root endpoint that returns server status
- GET /run-task: Endpoint that executes the task function from utils.py
"""

from fastapi import FastAPI
from utils import run_task

app = FastAPI()


@app.get("/")
def root_endpoint():
    """
    Endpoint for the root URL that returns server status.

    Returns:
        dict: A message confirming the server has started successfully.
    """
    return {"message": "Server started successfully!"}


@app.get("/run-task")
def run_task_endpoint():
    """
    Endpoint to run the task with a 3-second delay.

    Returns:
        dict: A message confirming the task has completed.
    """
    run_task(wait_time=3)
    return {"message": "Task completed successfully"}

