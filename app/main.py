from fastapi import FastAPI
from app.api.v1.endpoints import auth  # Import routes
from app.api.v1.endpoints import profile  # Import routes
from app.db.database import engine
from app.db.database import Base


# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(auth.router, prefix="/users", tags=["Users"])
app.include_router(profile.router, prefix="/profile", tags=["UserProfile"])

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}
