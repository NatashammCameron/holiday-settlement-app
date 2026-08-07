from fastapi import FastAPI
from app.routes.holiday_routes import router as holiday_router
from app.database.database import Base, engine
from app.models.holiday import Holiday

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(holiday_router)


@app.get("/")
def home():
    return {
        "message": "Holiday Settlement API is running"
    }