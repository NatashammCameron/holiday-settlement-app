from fastapi import FastAPI
from app.routes.holiday_routes import router as holiday_router
from app.database.database import Base, engine
from app.models.holiday import Holiday
from app.models.participant import Participant
from app.models.expense import Expense
from app.routes.expense_routes import router as expense_router
from app.routes.participant_routes import (
    router as participant_router
)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(holiday_router)


@app.get("/")
def home():
    return {
        "message": "Holiday Settlement API is running"
    }

app = FastAPI(
    title="Holiday Settlement API",
    version="1.0.0"
)

app.include_router(holiday_router)
app.include_router(participant_router)
app.include_router(expense_router)