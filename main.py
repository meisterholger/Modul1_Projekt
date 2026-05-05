"""
FastAPI application entry point.

This module runs the FastAPI application using Uvicorn server.
The application and its endpoints are defined in app/api.py.
"""

# Third-party imports
import uvicorn


if __name__ == "__main__":
    print("Program started.")

    # Run the FastAPI app using Uvicorn
    uvicorn.run("app.api:app", reload=True)

    # Print a message to indicate the end of the program
    print("Program ended successfully.")

