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
    assert result["message"] == "Found 3 matches"
    assert set(result["result"]["word_filter"]) == {"test", "testing", "contest"}


def test_run_task_filter_simple():
    """Test run_task with filter task and simple input."""
    task_data = {"word": "test", "word_list": ["test", "testing"]}
    result = run_task("filter", task_data)

    assert result["task"] == "filter"
    assert result["status"] == "success"
    assert result["message"] == "Found 2 matches"
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

    assert result["status"] == "error"
    assert result["message"] == "task type not found"
    assert result["result"] is None


def test_run_task_filter_no_matches():
    """Test run_task filter with no matching words."""
    task_data = {"word": "xyz", "word_list": ["test", "testing", "example"]}
    result = run_task("filter", task_data)

    assert result["task"] == "filter"
    assert result["status"] == "success"
    assert result["message"] == "Found 0 matches"
    assert result["result"]["word_filter"] is None


def test_run_task_steps_zero():
    """Test run_task steps with zero steps."""
    task_data = {"steps": 0}
    result = run_task("steps", task_data)

    assert result["task"] == "steps"
    assert result["status"] == "success"
    assert result["message"] == "no steps created"
    assert result["result"]["step_list"] is None


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
    assert result["status"] == "success"
    assert result["result"]["sum_squared"] == 0
    assert result["result"]["average_squared"] == 0


# ============================================================================
# Tests for task_data validation (missing required keys)
# ============================================================================


def test_run_task_filter_missing_word_key():
    """Test run_task filter with missing 'word' key."""
    task_data = {"word_list": ["test", "testing"]}  # Missing 'word'
    result = run_task("filter", task_data)

    assert result["status"] == "error"
    assert "Missing required key: word" in result["message"]
    assert result["result"] is None


def test_run_task_filter_missing_word_list_key():
    """Test run_task filter with missing 'word_list' key."""
    task_data = {"word": "test"}  # Missing 'word_list'
    result = run_task("filter", task_data)

    assert result["status"] == "error"
    assert "Missing required key: word_list" in result["message"]
    assert result["result"] is None


def test_run_task_steps_missing_steps_key():
    """Test run_task steps with missing 'steps' key."""
    task_data = {}  # Missing 'steps'
    result = run_task("steps", task_data)

    assert result["status"] == "error"
    assert "Missing required key: steps" in result["message"]
    assert result["result"] is None


def test_run_task_batch_missing_list_numbers_key():
    """Test run_task batch with missing 'list_numbers' key."""
    task_data = {}  # Missing 'list_numbers'
    result = run_task("batch", task_data)

    assert result["status"] == "error"
    assert "Missing required key: list_numbers" in result["message"]
    assert result["result"] is None


def test_run_task_filter_all_keys_missing():
    """Test run_task filter with all keys missing."""
    task_data = {}
    result = run_task("filter", task_data)

    # Should report first missing key
    assert result["status"] == "error"
    assert "Missing required key:" in result["message"]
    assert result["result"] is None


def test_string_filter_basic():
    """Test string_filter function directly."""
    test_data = {
        "word": "test",
        "word_list": ["test", "testing", "example", "best", "contest"],
    }
    result = string_filter(test_data)

    assert result["status"] == "success"
    assert result["message"] == "Found 3 matches"
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

    assert result["status"] == "success"
    assert result["message"] == "no steps created"
    assert result["data"]["step_list"] is None


def test_step_processing_negative():
    """Test step_processing with negative number."""
    test_data = {"steps": -3}
    result = step_processing(test_data)

    assert result["status"] == "success"
    assert result["message"] == "no steps created"
    assert result["data"]["step_list"] is None


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

    assert result["status"] == "success"
    assert result["message"] is None
    assert result["data"]["sum_squared"] == 0
    assert result["data"]["average_squared"] == 0


# ============================================================================
# Tests for type validation and error cases
# ============================================================================


def test_string_filter_invalid_word_type():
    """Test string_filter with non-string word parameter."""
    test_data = {"word": 123, "word_list": ["test", "example"]}
    result = run_task("filter", test_data)

    assert result["status"] == "error"
    assert result["message"] == "filter values must be strings"
    assert result["result"]["word_filter"] is None


def test_string_filter_invalid_list_type():
    """Test string_filter with non-string items in word_list."""
    test_data = {"word": "test", "word_list": ["test", 123, "example"]}
    result = run_task("filter", test_data)

    assert result["status"] == "error"
    assert result["message"] == "filter values must be strings"
    assert result["result"]["word_filter"] is None


def test_step_processing_invalid_type():
    """Test step_processing with non-integer steps."""
    test_data = {"steps": "five"}
    result = run_task("steps", test_data)

    assert result["status"] == "error"
    assert result["message"] == "steps must be an integer"
    assert result["result"]["step_list"] is None


def test_step_processing_float_type():
    """Test step_processing with float instead of integer."""
    test_data = {"steps": 5.5}
    result = run_task("steps", test_data)

    assert result["status"] == "error"
    assert result["message"] == "steps must be an integer"
    assert result["result"]["step_list"] is None


def test_calculate_square_with_floats():
    """Test calculate_square function with float values."""
    test_data = {"list_numbers": [1.5, 2.5, 3.0]}
    result = run_task("batch", test_data)

    assert result["status"] == "success"
    assert result["message"] is None
    # 1.5^2 + 2.5^2 + 3.0^2 = 2.25 + 6.25 + 9.0 = 17.5
    assert result["result"]["sum_squared"] == pytest.approx(17.5)
    assert result["result"]["average_squared"] == pytest.approx(17.5 / 3)


def test_calculate_square_mixed_int_float():
    """Test calculate_square with mixed int and float values."""
    test_data = {"list_numbers": [1, 2.5, 3]}
    result = run_task("batch", test_data)

    assert result["status"] == "success"
    # 1 + 6.25 + 9 = 16.25
    assert result["result"]["sum_squared"] == pytest.approx(16.25)


def test_calculate_square_invalid_type():
    """Test calculate_square with invalid type in list."""
    test_data = {"list_numbers": [1, 2, "three", 4]}
    result = run_task("batch", test_data)

    assert result["status"] == "error"
    assert result["message"] == "numbers must be int or float"
    assert result["result"]["dict_squared"] is None
    assert result["result"]["sum_squared"] is None
    assert result["result"]["average_squared"] is None


def test_calculate_square_not_a_list():
    """Test calculate_square with non-list input."""
    test_data = {"list_numbers": "not a list"}
    result = run_task("batch", test_data)

    assert result["status"] == "error"
    assert result["message"] == "numbers must be int or float"
    assert result["result"]["dict_squared"] is None
    assert result["result"]["sum_squared"] is None
    assert result["result"]["average_squared"] is None


def test_run_task_batch_floats():
    """Test run_task batch with float values."""
    task_data = {"list_numbers": [1.0, 2.0, 3.0, 4.0]}
    result = run_task("batch", task_data)

    assert result["task"] == "batch"
    assert result["status"] == "success"
    assert result["result"]["sum_squared"] == pytest.approx(30.0)
    assert result["result"]["average_squared"] == pytest.approx(7.5)
