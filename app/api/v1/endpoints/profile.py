from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.middleware.verifyToken import verify_token

router = APIRouter()

@router.get("/")
def get_profile(
    current_user: User = Depends(verify_token), 
    db: Session = Depends(get_db)
):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    # Return user profile data
    return {
        "user": {
            "id": current_user.id,
            "name": current_user.name,
            "email": current_user.email
        }
    }
