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


def string_filter(word: str, list_with_words: list):
    """Filters a list of words based on a given word.

    Args:
        word (str): The word to filter by.
        list_with_words (list): The list of words to filter.

    Returns:
        word_filter (list): A list of words that contain the given word.
        word_count (int): The number of words that contain the given word.
    """
    word_filter = [w for w in list_with_words if w.find(word) != -1]
    word_count = len(word_filter)
    return word_filter, word_count


def step_processing(steps: int):
    """
    Creates a step based on the number of steps provided.

    Args:
        steps (int): The number of steps to create.

    Returns:
        step_list (list): A list of step messages.
    """
    step_list = [f"Step {i}" for i in range(1, steps + 1)]
    return step_list


def calculate_square(list_numbers: list):
    """
    Calculates the square of each number in a given list.

    Args:
        list_numbers (list): A list of numbers to be squared.

    Returns:
        list: A list of squared numbers.
    """
    dict_squared = [{"input": num, "output": num**2} for num in list_numbers]

    sum_squared = sum(item["output"] for item in dict_squared)
    average_squared = sum_squared / len(dict_squared) if dict_squared else 0
    return dict_squared, sum_squared, average_squared
