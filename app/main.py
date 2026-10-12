import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/info")
def info():
    return {
        "app": "status-api",
        "version": "0.1.0",
        "environment": os.getenv("APP_ENV", "development"),
    }
