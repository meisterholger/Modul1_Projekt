"""
This module contains utility functions that can be used in various parts of the project.
In this case, it contains a function `run_task` that prints a message
indicating the start and end of a task, with a delay in between.
"""


def string_filter(word: str, list_with_words: list) -> dict:
    """Filter a list of words based on a given word.

    Args:
        word (str): The word to filter by.
        list_with_words (list): The list of words to filter.

    Returns:
        dict: Task result containing filtered words and count.
    """
    word_filter = [w for w in list_with_words if word in w]
    word_count = len(word_filter)
    task_result = {
        "task": "filter",
        "result": {"word_filter": word_filter, "word_count": word_count},
        "status": "success" if word_filter else "no words found",
    }
    return task_result


def step_processing(steps: int) -> dict:
    """Generate a sequence of step labels.

    Args:
        steps (int): The number of steps to generate.

    Returns:
        dict: Task result containing the list of step labels.
    """
    step_list = [f"Step {i}" for i in range(1, steps + 1)]
    task_result = {
        "task": "steps",
        "result": {"step_list": step_list},
        "status": "success" if step_list else "no steps created",
    }
    return task_result


def calculate_square(list_numbers: list) -> dict:
    """Calculate statistics on squared numbers.

    Computes the square of each number and calculates sum and average.

    Args:
        list_numbers (list): A list of numbers to be squared.

    Returns:
        dict: Task result containing squared values and their statistics.
    """
    dict_squared = [{"input": num, "output": num**2} for num in list_numbers]

    sum_squared = sum(item["output"] for item in dict_squared)
    average_squared = sum_squared / len(dict_squared) if dict_squared else 0

    task_result = {
        "task": "batch",
        "result": {
            "dict_squared": dict_squared,
            "sum_squared": sum_squared,
            "average_squared": average_squared,
        },
        "status": "success" if dict_squared else "no numbers provided",
    }

    return task_result


# Mapping of functions
tasks = {
    "filter": string_filter,
    "steps": step_processing,
    "batch": calculate_square,
}


# Function definition
def run_task(task_type: str, data) -> dict:
    """Execute a task function based on the type and provided data.

    Handles task execution with error handling and always returns a dict.

    Args:
        task_type (str): The type of task to run ("filter", "steps", or "batch").
        data: The data to be processed by the task function.

    Returns:
        dict: Task result with status and output, or error information.
    """
    print("Task started")
    try:
        if task_type not in tasks:
            return {
                "task": task_type,
                "result": None,
                "status": "error: task type not found",
            }

        data_processed = data if isinstance(data, tuple) else (data,)
        task_result = tasks[task_type](*data_processed)
        return task_result
    except (TypeError, ValueError, IndexError) as e:
        task_result = {
            "task": task_type,
            "result": None,
            "status": f"error: {e}",
        }
        return task_result
    finally:
        print("Task completed")
