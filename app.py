"""
FastAPI application module.
This module creates and configures the FastAPI application instance.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    Root endpoint that returns a message indicating the server is running.
    
    Returns:
        dict: A dictionary with a success message.
    """
    return {"message": "Server is running!"}
