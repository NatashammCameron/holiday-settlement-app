from fastapi import FastAPI

from app.database.database import Base, engine
from app.models.holiday import Holiday

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Holiday Settlement API is running"
    }
