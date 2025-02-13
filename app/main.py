from fastapi import FastAPI
from app.api.v1.endpoints.auth import router as auth_router
from .db.database import engine, Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include authentication routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Authentication"}
