from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    return {"message": "List of users"}

@router.post("/")
def create_user():
    return {"message": "User created"}
