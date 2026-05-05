"""
Entry point for the program. Functions from utils.py are called here.
Start the FastAPI app. The run_task function is controlled by a FastAPI endpoint,
so it is not called directly in this file.
"""

# Third-party imports
import uvicorn
from fastapi import FastAPI
from utils import run_task

app = FastAPI()

@app.get("/")
def run_task_endpoint():
    """
    Endpoint to run the task with a 3-second delay.
    
    Returns:
        dict: A message confirming the task has completed.
    """
    return {"message": "Server started successfully!"}

@app.get("/run-task")
def run_task_endpoint():
    """
    Endpoint to run the task with a 3-second delay.
    
    Returns:
        dict: A message confirming the task has completed.
    """
    run_task(wait_time=3)
    return {"message": "Task completed successfully"}


if __name__ == "__main__":
    print("Program started.")

    # Run the FastAPI app using Uvicorn
    uvicorn.run("main:app", reload=True)

    # Print a message to indicate the end of the program
    print("Program ended successfully.")
