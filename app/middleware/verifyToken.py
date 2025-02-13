# from fastapi import HTTPException, status, Depends, Request
# from jose import JWTError, jwt
# from datetime import datetime, timedelta
# from typing import Optional
# from sqlalchemy.orm import Session  # Fix: Import Session
# from app.db.database import get_db
# from app.models.user import User  # Replace with your User model

# SECRET_KEY = "Pass@1234"  # Replace with your secret key
# ALGORITHM = "HS256"

# def verify_token(request: Request, db: Session = Depends(get_db)) -> User:
#     auth_header = request.headers.get("Authorization")
    
#     if not auth_header or not auth_header.startswith("Bearer "):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Unauthorized: Missing or malformed Authorization header"
#         )

#     token = auth_header.split(" ")[1]  # Extract token
    
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id = payload.get("id")
#         user_email = payload.get("email")
        
#         if not user_id or not user_email:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Unauthorized: Invalid token payload"
#             )

#         user = db.query(User).filter(User.id == user_id, User.email == user_email).first()
        
#         if user is None:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Unauthorized: User not found"
#             )

#         return user
#     except JWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Unauthorized: Token invalid or expired"
#         )
