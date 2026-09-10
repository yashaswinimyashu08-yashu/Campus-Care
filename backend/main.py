from fastapi import FastAPI

app = FastAPI(title="CampusCare API")


@app.get("/")
def home():
    return {"message": "CampusCare API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}