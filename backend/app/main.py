from fastapi import FastAPI

from app.database.database import Base, engine

from app.models.holiday import Holiday
from app.models.participant import Participant
from app.models.expense import Expense
from app.models.expense_split import ExpenseSplit
from app.models.user import User

from app.routes.holiday_routes import router as holiday_router
from app.routes.participant_routes import router as participant_router
from app.routes.expense_routes import router as expense_router
from app.routes.settlement_routes import router as settlement_router
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth_routes import (
    router as auth_router
)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Holiday Settlement API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Holiday Settlement API is running"
    }


app.include_router(holiday_router)
app.include_router(participant_router)
app.include_router(expense_router)
app.include_router(settlement_router)
app.include_router(auth_router)