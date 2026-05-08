"""Tests for the FastAPI application endpoints."""

import pytest
from fastapi.testclient import TestClient

from app.api import app


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


# ============================================================================
# Tests for /run-task endpoint (POST)
# ============================================================================


def test_run_task_filter_endpoint():
    """Test the /run-task endpoint with filter task type."""
    client = TestClient(app)
    request_data = {
        "task_type": "filter",
        "task_data": {"word": "test", "word_list": ["test", "testing", "example"]},
    }
    response = client.post("/run-task", json=request_data)

    assert response.status_code == 200
    result = response.json()
    assert result["task"] == "filter"
    assert result["status"] == "success"
    assert result["message"] == "Found 2 matches"
    assert result["result"]["word_filter"] == ["test", "testing"]


def test_run_task_steps_endpoint():
    """Test the /run-task endpoint with steps task type."""
    client = TestClient(app)
    request_data = {"task_type": "steps", "task_data": {"steps": 3}}
    response = client.post("/run-task", json=request_data)

    assert response.status_code == 200
    result = response.json()
    assert result["task"] == "steps"
    assert result["status"] == "success"
    assert result["message"] is None
    assert result["result"]["step_list"] == ["Step 1", "Step 2", "Step 3"]


def test_run_task_batch_endpoint():
    """Test the /run-task endpoint with batch task type."""
    client = TestClient(app)
    request_data = {"task_type": "batch", "task_data": {"list_numbers": [1, 2, 3]}}
    response = client.post("/run-task", json=request_data)

    assert response.status_code == 200
    result = response.json()
    assert result["task"] == "batch"
    assert result["status"] == "success"
    assert result["message"] is None
    assert result["result"]["sum_squared"] == 14  # 1 + 4 + 9
    assert result["result"]["average_squared"] == pytest.approx(14 / 3)


def test_run_task_invalid_task_type_endpoint():
    """Test the /run-task endpoint with invalid task type."""
    client = TestClient(app)
    request_data = {
        "task_type": "invalid_type",
        "task_data": {"some_key": "some_value"},
    }
    response = client.post("/run-task", json=request_data)

    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "error"
    assert result["message"] == "task type not found"
    assert result["result"] is None


def test_run_task_filter_error_endpoint():
    """Test the /run-task endpoint with invalid filter data."""
    client = TestClient(app)
    request_data = {
        "task_type": "filter",
        "task_data": {"word": 123, "word_list": ["test", "example"]},
    }
    response = client.post("/run-task", json=request_data)

    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "error"
    assert result["message"] == "filter values must be strings"
    assert result["result"]["word_filter"] is None


def test_run_task_missing_required_key_endpoint():
    """Test the /run-task endpoint with missing required key."""
    client = TestClient(app)
    request_data = {
        "task_type": "filter",
        "task_data": {"word": "test"},
    }  # Missing word_list

    response = client.post("/run-task", json=request_data)

    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "error"
    assert "Missing required key" in result["message"]
    assert result["result"] is None


def test_run_task_missing_request_field():
    """Test the /run-task endpoint with missing request field."""
    client = TestClient(app)
    request_data = {"task_type": "filter"}  # Missing task_data

    response = client.post("/run-task", json=request_data)

    assert response.status_code == 422  # Validation error
