"""Tests for utility functions."""

import pytest
from app.utils import run_task, string_filter, step_processing, calculate_square


# ============================================================================
# Tests for run_task (Orchestrator)
# ============================================================================


def test_run_task_filter_basic():
    """Test run_task with filter task and multiple words."""
    result = run_task(
        "filter", ("test", ["test", "testing", "example", "best", "contest"])
    )

    assert result["task"] == "filter"
    assert result["status"] == "success"
    assert result["result"]["word_count"] == 3
    assert set(result["result"]["word_filter"]) == {"test", "testing", "contest"}


def test_run_task_filter_simple():
    """Test run_task with filter task and simple input."""
    result = run_task("filter", ("test", ["test", "testing"]))

    assert result["task"] == "filter"
    assert result["status"] == "success"
    assert result["result"]["word_count"] == 2
    assert result["result"]["word_filter"] == ["test", "testing"]


def test_run_task_steps_basic():
    """Test run_task with steps task."""
    result = run_task("steps", 5)

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
    result = run_task("batch", [1, 2, 3, 4, 5])

    assert result["task"] == "batch"
    assert result["status"] == "success"
    assert result["result"]["sum_squared"] == 55  # 1 + 4 + 9 + 16 + 25
    assert result["result"]["average_squared"] == pytest.approx(11.0)  # 55 / 5


def test_run_task_invalid_task_type():
    """Test run_task with invalid task type."""
    result = run_task("invalid_task", [])

    assert result["status"] == "error: task type not found"
    assert result["result"] is None


def test_run_task_filter_no_matches():
    """Test run_task filter with no matching words."""
    result = run_task("filter", ("xyz", ["test", "testing", "example"]))

    assert result["task"] == "filter"
    assert result["status"] == "no words found"
    assert result["result"]["word_filter"] == []
    assert result["result"]["word_count"] == 0


def test_run_task_steps_zero():
    """Test run_task steps with zero steps."""
    result = run_task("steps", 0)

    assert result["task"] == "steps"
    assert result["status"] == "no steps created"
    assert result["result"]["step_list"] == []


def test_run_task_batch_single_number():
    """Test run_task batch with single number."""
    result = run_task("batch", [3])

    assert result["task"] == "batch"
    assert result["status"] == "success"
    assert result["result"]["sum_squared"] == 9
    assert result["result"]["average_squared"] == 9.0


def test_run_task_batch_empty():
    """Test run_task batch with empty list."""
    result = run_task("batch", [])

    assert result["task"] == "batch"
    assert result["status"] == "no numbers provided"
    assert result["result"]["dict_squared"] == []
    assert result["result"]["sum_squared"] == 0
    assert result["result"]["average_squared"] == 0


# ============================================================================
# Tests for individual functions (direct calls)
# ============================================================================


def test_string_filter_basic():
    """Test string_filter function directly."""
    result = string_filter("test", ["test", "testing", "example", "best", "contest"])

    assert result["task"] == "filter"
    assert result["status"] == "success"
    assert result["result"]["word_count"] == 3
    assert set(result["result"]["word_filter"]) == {"test", "testing", "contest"}


def test_step_processing_basic():
    """Test step_processing function directly."""
    result = step_processing(5)

    assert result["task"] == "steps"
    assert result["status"] == "success"
    assert result["result"]["step_list"] == [
        "Step 1",
        "Step 2",
        "Step 3",
        "Step 4",
        "Step 5",
    ]


def test_step_processing_zero():
    """Test step_processing with zero."""
    result = step_processing(0)

    assert result["status"] == "no steps created"
    assert result["result"]["step_list"] == []


def test_step_processing_negative():
    """Test step_processing with negative number."""
    result = step_processing(-3)

    assert result["status"] == "no steps created"
    assert result["result"]["step_list"] == []


def test_calculate_square_basic():
    """Test calculate_square function directly."""
    result = calculate_square([1, 2, 3, 4])

    assert result["task"] == "batch"
    assert result["status"] == "success"
    assert result["result"]["sum_squared"] == 30  # 1 + 4 + 9 + 16
    assert result["result"]["average_squared"] == pytest.approx(7.5)
    assert len(result["result"]["dict_squared"]) == 4


def test_calculate_square_single():
    """Test calculate_square with single number."""
    result = calculate_square([5])

    assert result["result"]["sum_squared"] == 25
    assert result["result"]["average_squared"] == 25.0
    assert result["result"]["dict_squared"][0] == {"input": 5, "output": 25}


def test_calculate_square_empty():
    """Test calculate_square with empty list."""
    result = calculate_square([])

    assert result["status"] == "no numbers provided"
    assert result["result"]["sum_squared"] == 0
    assert result["result"]["average_squared"] == 0
