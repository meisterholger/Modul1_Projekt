import pytest
from fastapi.testclient import TestClient

from app import app

def test_root_endpoint():
    """
    Test the root endpoint to ensure it returns the expected message.

    This test will send a GET request to the root endpoint and check that
    the response status code is 200 and that the returned JSON contains
    the correct message.
    """
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server started successfully!"}

def test_run_task_endpoint():
    """
    Test the /run-task endpoint to ensure it executes the task and returns the expected message.

    This test will send a GET request to the /run-task endpoint and check that
    the response status code is 200 and that the returned JSON contains
    the correct message indicating task completion.
    """
    client = TestClient(app)
    response = client.get("/run-task")
    assert response.status_code == 200
    assert response.json() == {"message": "Task completed successfully"}