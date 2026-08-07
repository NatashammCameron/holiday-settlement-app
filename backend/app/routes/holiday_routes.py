from fastapi import APIRouter

router = APIRouter(
    prefix="/holidays",
    tags=["Holidays"]
)


@router.get("/")
def get_holidays():
    return {
        "message": "Holiday router working"
    }