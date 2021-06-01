from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def customer():
    return {"Hello": "World"}
