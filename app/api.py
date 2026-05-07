"""
FastAPI application module.
This module creates and configures the FastAPI application instance,
defining two endpoints:
- GET /: Root endpoint that returns server status
- GET /run-task: Endpoint that executes the task function from utils.py
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root_endpoint():
    """
    Endpoint for the root URL that returns server status.

    Returns:
        dict: A message confirming the server has started successfully.
    """
    return {"message": "Server started successfully!"}


# @app.get("/run-task")
# def run_task_endpoint():
#     """
#     Endpoint to execute a task.
#     TODO: Implement with query parameters for flexible task execution.
#     """
#     pass
