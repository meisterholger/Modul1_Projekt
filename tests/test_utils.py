import pytest
from app.utils import run_task


def test_run_task():
    """
    Test the run_task function to ensure it executes without errors.

    This test will call the run_task function with a short wait time and
    check that it completes successfully. Since run_task prints output to
    the console, we will not capture the output in this test, but we will
    ensure that the function runs without raising any exceptions.
    """
    try:
        run_task(wait_time=1)  # Use a shorter wait time for testing
        assert True  # If no exceptions are raised, the test passes
    except Exception as e:
        pytest.fail(f"run_task raised an exception: {e}")