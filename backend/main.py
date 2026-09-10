from fastapi import FastAPI
from sqlalchemy import text

from backend.database import engine

app = FastAPI(title="CampusCare API")


@app.get("/")
def home():
    return {"message": "CampusCare API is running"}


@app.get("/health")
def health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected",
    }