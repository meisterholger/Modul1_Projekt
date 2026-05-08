"""Task processing utility module.

Provides functions for executing various data processing tasks through
a centralized orchestrator (run_task) that handles task routing and response formatting.
"""

# Task Data Format Specification
# Defines the required keys for each task type's input dictionary
TASK_DATA_SPECS = {
    "filter": ["word", "word_list"],
    "steps": ["steps"],
    "batch": ["list_numbers"],
}


def string_filter(task_data: dict) -> dict:
    """Filter a list of words based on a given word.

    Args:
        task_data (dict): Dictionary containing 'word' and 'word_list' keys.
            - word (str): The word to filter by.
            - word_list (list): The list of words to filter.

    Returns:
        dict: Task result containing filtered words and count.
    """
    word = task_data["word"]
    list_with_words = task_data["word_list"]
    # Guard Clause
    if not isinstance(word, str) or not all(
        isinstance(w, str) for w in list_with_words
    ):
        task_result = {
            "data": {"word_filter": None},
            "status": "error",
            "message": "filter values must be strings",
        }
        return task_result

    # In case the Guard Clause is not triggered:
    word_filter = [w for w in list_with_words if word in w]
    word_count = len(word_filter)
    task_result = {
        "data": {"word_filter": word_filter if word_filter else None},
        "status": "success",
        "message": f"Found {word_count} matches",
    }
    return task_result


def step_processing(task_data: dict) -> dict:
    """Generate a sequence of step labels.

    Args:
        task_data (dict): Dictionary containing 'steps' key.
            - steps (int): The number of steps to generate.

    Returns:
        dict: Task result containing the list of step labels.
    """
    steps = task_data["steps"]
    # Guard Clause
    if not isinstance(steps, int):
        task_result = {
            "data": {"step_list": None},
            "status": "error",
            "message": "steps must be an integer",
        }
        return task_result
    # In case the Guard Clause is not triggered:
    step_list = [f"Step {i}" for i in range(1, steps + 1)]
    task_result = {
        "data": {"step_list": step_list if step_list else None},
        "status": "success",
        "message": None if step_list else "no steps created",
    }
    return task_result


def calculate_square(task_data: dict) -> dict:
    """Calculate statistics on squared numbers.

    Computes the square of each number and calculates sum and average.

    Args:
        task_data (dict): Dictionary containing 'list_numbers' key.
            - list_numbers (list): A list of numbers to be squared.

    Returns:
        dict: Task result containing squared values and their statistics.
    """
    list_numbers = task_data["list_numbers"]
    # Guard Clause
    if not isinstance(list_numbers, list) or not all(
        isinstance(num, (int, float)) for num in list_numbers
    ):
        task_result = {
            "data": {
                "dict_squared": None,
                "sum_squared": None,
                "average_squared": None,
            },
            "status": "error",
            "message": "numbers must be int or float",
        }
        return task_result
    # In case the Guard Clause is not triggered:
    dict_squared = [{"input": num, "output": num**2} for num in list_numbers]
    sum_squared = sum(item["output"] for item in dict_squared)
    average_squared = sum_squared / len(dict_squared) if dict_squared else 0

    task_result = {
        "data": {
            "dict_squared": dict_squared,
            "sum_squared": sum_squared,
            "average_squared": average_squared,
        },
        "status": "success",
        "message": None,
    }
    return task_result


# Mapping of functions
tasks = {
    "filter": string_filter,
    "steps": step_processing,
    "batch": calculate_square,
}


# Function definition
def run_task(task_type: str, task_data: dict) -> dict:
    """Execute a task function based on the type and provided data.

    Handles task execution with error handling and always returns a dict.

    Args:
        task_type (str): The type of task to run ("filter", "steps", or "batch").
        task_data (dict): The data to be processed by the task function.
            See TASK_DATA_SPECS for required keys per task type.

    Returns:
        dict: Task result with status and output, or error information.
    """
    print("Task started")
    try:
        if task_type not in tasks:
            return {
                "task": task_type,
                "result": None,
                "status": "error",
                "message": "task type not found",
            }
        if task_type in TASK_DATA_SPECS:
            required_keys = TASK_DATA_SPECS[task_type]
            for key in required_keys:
                if key not in task_data:
                    raise ValueError(f"Missing required key: {key}")

        task_result = tasks[task_type](task_data)
        response = {
            "task": task_type,
            "status": task_result["status"],
            "message": task_result["message"],
            "result": task_result["data"],
        }
        return response
    except (TypeError, ValueError, IndexError) as e:
        return {
            "task": task_type,
            "status": "error",
            "message": str(e),
            "result": None,
        }
    finally:
        print("Task completed")
