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
    # host="0.0.0.0" allows external access (necessary for Docker)
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)

    # Print a message to indicate the end of the program
    print("Program ended successfully.")

