"""Tests for utility functions."""

import pytest
from app.utils import run_task, string_filter, step_processing, calculate_square


def test_run_task():
    """
    Test the run_task function to ensure it executes without errors.

    This test will call the run_task function with a short wait time and
    check that it completes successfully. Since run_task prints output to
    the console, we will not capture the output in this test, but we will
    ensure that the function runs without raising any exceptions.
    """
    run_task(wait_time=1)  # Use a shorter wait time for testing
    assert True  # Test passes if no exceptions are raised


def test_string_filter():
    """
    Test the string_filter function to ensure it correctly filters a list of words.

    This test will call the string_filter function with a sample word and a list of words,
    and check that the returned list contains only the words that include the sample word.
    """
    sample_word = "test"
    word_list = ["test", "testing", "example", "best", "contest"]
    expected_output = ["test", "testing", "contest"]

    result, count = string_filter(sample_word, word_list)
    assert result == expected_output
    assert count == len(expected_output)


def test_step_processing_5():
    """
    Test the step_processing function to ensure it creates the correct list of steps.

    This test will call the step_processing function with a specific number of steps and
    check that the returned list contains the correct step messages.
    """
    steps = 5
    expected_output = ["Step 1", "Step 2", "Step 3", "Step 4", "Step 5"]

    result = step_processing(steps)
    assert result == expected_output


def test_step_processing_0():
    """
    Test the step_processing function to ensure it creates the correct list of steps.

    This test will call the step_processing function with a specific number of steps and
    check that the returned list contains the correct step messages.
    """
    steps = 0
    expected_output = []

    result = step_processing(steps)
    assert result == expected_output


def test_step_processing_negative():
    """
    Test the step_processing function to ensure it creates the correct list of steps.

    This test will call the step_processing function with a specific number of steps and
    check that the returned list contains the correct step messages.
    """
    steps = -3
    expected_output = []

    result = step_processing(steps)
    assert result == expected_output


def test_calculate_square_4():
    """
    Test the calculate_square function to ensure it correctly calculates the squares of numbers.

    This test will call the calculate_square function with a list of numbers and
    check that the returned list contains the correct squares of those numbers.
    """
    numbers = [1, 2, 3, 4]
    expected_output = [
        {"input": 1, "output": 1},
        {"input": 2, "output": 4},
        {"input": 3, "output": 9},
        {"input": 4, "output": 16},
    ]

    list_squared, sum_squared, average_squared = calculate_square(numbers)
    print(sum_squared)
    assert list_squared == expected_output
    assert sum_squared == 30
    assert average_squared == pytest.approx(7.5)


def test_calculate_square_3():
    """
    Test the calculate_square function to ensure it correctly calculates the squares of numbers.

    This test will call the calculate_square function with a list of numbers and
    check that the returned list contains the correct squares of those numbers.
    """
    numbers = [1, 2, 3]
    expected_output = [
        {"input": 1, "output": 1},
        {"input": 2, "output": 4},
        {"input": 3, "output": 9},
    ]

    list_squared, sum_squared, average_squared = calculate_square(numbers)
    print(sum_squared)
    assert list_squared == expected_output
    assert sum_squared == 14
    assert average_squared == pytest.approx(14 / 3)
