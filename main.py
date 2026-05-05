"""
Entry point for the program. Functions from utils.py are called here.
Start the FastAPI app. The run_task function is controlled by a FastAPI endpoint,
so it is not called directly in this file.
"""

# Third-party imports
import uvicorn


if __name__ == "__main__":
    print("Program started.")

    # Run the FastAPI app using Uvicorn
    uvicorn.run("app:app", reload=True)

    # run_task(wait_time=3) -- Will be controlled by FastAPI endpoint, so it's
    # commented out here.

    # Print a message to indicate the end of the program
    print("Program ended successfully.")
