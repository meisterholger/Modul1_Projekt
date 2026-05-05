"""
This module contains utility functions that can be used in various parts of the project.
In this case, it contains a function `run_task` that prints a message
indicating the start and end of a task, with a delay in between.
"""

# Import the time module to use the sleep function
import time

# Function definition


def run_task(wait_time=2):
    """
    Prints a message indicating the start and end of a task, with a delay in between.

    Args:
        wait_time (int): The amount of time (in seconds) to wait
        between the start and end messages. Default is 2 seconds.
    """
    print("Task started")
    print(f"Task running for {wait_time} seconds...")
    time.sleep(wait_time)
    print("Task completed")
