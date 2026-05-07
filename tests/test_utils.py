"""Tests for utility functions."""

import pytest
from app.utils import run_task, string_filter, step_processing, calculate_square


# ============================================================================
# Tests for run_task (Orchestrator)
# ============================================================================


def test_run_task_filter_basic():
    """Test run_task with filter task and multiple words."""
    task_data = {
        "word": "test",
        "word_list": ["test", "testing", "example", "best", "contest"],
    }
    result = run_task("filter", task_data)

    assert result["task"] == "filter"
    assert result["status"] == "success"
    assert result["result"]["word_count"] == 3
    assert set(result["result"]["word_filter"]) == {"test", "testing", "contest"}


def test_run_task_filter_simple():
    """Test run_task with filter task and simple input."""
    task_data = {"word": "test", "word_list": ["test", "testing"]}
    result = run_task("filter", task_data)

    assert result["task"] == "filter"
    assert result["status"] == "success"
    assert result["result"]["word_count"] == 2
    assert result["result"]["word_filter"] == ["test", "testing"]


def test_run_task_steps_basic():
    """Test run_task with steps task."""
    task_data = {"steps": 5}
    result = run_task("steps", task_data)

    assert result["task"] == "steps"
    assert result["status"] == "success"
    assert result["result"]["step_list"] == [
        "Step 1",
        "Step 2",
        "Step 3",
        "Step 4",
        "Step 5",
    ]


def test_run_task_batch_basic():
    """Test run_task with batch task."""
    task_data = {"list_numbers": [1, 2, 3, 4, 5]}
    result = run_task("batch", task_data)

    assert result["task"] == "batch"
    assert result["status"] == "success"
    assert result["result"]["sum_squared"] == 55  # 1 + 4 + 9 + 16 + 25
    assert result["result"]["average_squared"] == pytest.approx(11.0)  # 55 / 5


def test_run_task_invalid_task_type():
    """Test run_task with invalid task type."""
    task_data = {"some_key": "some_value"}
    result = run_task("invalid_task", task_data)

    assert result["status"] == "error: task type not found"
    assert result["result"] is None


def test_run_task_filter_no_matches():
    """Test run_task filter with no matching words."""
    task_data = {"word": "xyz", "word_list": ["test", "testing", "example"]}
    result = run_task("filter", task_data)

    assert result["task"] == "filter"
    assert result["status"] == "no words found"
    assert result["result"] is None


def test_run_task_steps_zero():
    """Test run_task steps with zero steps."""
    task_data = {"steps": 0}
    result = run_task("steps", task_data)

    assert result["task"] == "steps"
    assert result["status"] == "no steps created"
    assert result["result"] is None


def test_run_task_batch_single_number():
    """Test run_task batch with single number."""
    task_data = {"list_numbers": [3]}
    result = run_task("batch", task_data)

    assert result["task"] == "batch"
    assert result["status"] == "success"
    assert result["result"]["sum_squared"] == 9
    assert result["result"]["average_squared"] == 9.0


def test_run_task_batch_empty():
    """Test run_task batch with empty list."""
    task_data = {"list_numbers": []}
    result = run_task("batch", task_data)

    assert result["task"] == "batch"
    assert result["status"] == "no numbers provided"
    assert result["result"] is None


# ============================================================================
# Tests for individual functions (direct calls)
# ============================================================================


def test_string_filter_basic():
    """Test string_filter function directly."""
    test_data = {
        "word": "test",
        "word_list": ["test", "testing", "example", "best", "contest"],
    }
    result = string_filter(test_data)

    assert result["status"] == "success"
    assert result["data"]["word_count"] == 3
    assert set(result["data"]["word_filter"]) == {"test", "testing", "contest"}


def test_step_processing_basic():
    """Test step_processing function directly."""
    test_data = {"steps": 5}
    result = step_processing(test_data)
    assert result["status"] == "success"
    assert result["data"]["step_list"] == [
        "Step 1",
        "Step 2",
        "Step 3",
        "Step 4",
        "Step 5",
    ]


def test_step_processing_zero():
    """Test step_processing with zero."""
    test_data = {"steps": 0}
    result = step_processing(test_data)

    assert result["status"] == "no steps created"
    assert result["data"]["step_list"] == []


def test_step_processing_negative():
    """Test step_processing with negative number."""
    test_data = {"steps": -3}
    result = step_processing(test_data)

    assert result["status"] == "no steps created"
    assert result["data"]["step_list"] == []


def test_calculate_square_basic():
    """Test calculate_square function directly."""
    test_data = {"list_numbers": [1, 2, 3, 4]}
    result = calculate_square(test_data)

    assert result["status"] == "success"
    assert result["data"]["sum_squared"] == 30  # 1 + 4 + 9 + 16
    assert result["data"]["average_squared"] == pytest.approx(7.5)
    assert len(result["data"]["dict_squared"]) == 4


def test_calculate_square_single():
    """Test calculate_square with single number."""
    test_data = {"list_numbers": [5]}
    result = calculate_square(test_data)

    assert result["data"]["sum_squared"] == 25
    assert result["data"]["average_squared"] == 25.0
    assert result["data"]["dict_squared"][0] == {"input": 5, "output": 25}


def test_calculate_square_empty():
    """Test calculate_square with empty list."""
    test_data = {"list_numbers": []}
    result = calculate_square(test_data)

    assert result["status"] == "no numbers provided"
    assert result["data"]["sum_squared"] == 0
    assert result["data"]["average_squared"] == 0
