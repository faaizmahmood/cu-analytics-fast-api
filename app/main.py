from fastapi import FastAPI
from app.api.v1.endpoints.auth import router as auth_router
from app.db.database import engine, Base
from app.tasks.tasks import add_numbers  # Import Celery task
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


# CORS
origins = [
    "http://localhost:5173",  # Example for React app running on localhost:3000
    "https://yourfrontenddomain.com",  # Replace with your actual frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins to make requests
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Create tables
Base.metadata.create_all(bind=engine)

# Include authentication routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Authentication"}

# New route to trigger Celery background task
@app.get("/add")
def run_task(x: int, y: int):
    task = add_numbers.apply_async(args=[x, y])  # Send task to Celery
    return {"task_id": task.id, "status": "Processing"}

# Check task result
from celery.result import AsyncResult
from app.worker.celery import celery

@app.get("/result/{task_id}")
def get_result(task_id: str):
    result = AsyncResult(task_id, app=celery)
    return {"task_status": result.status, "task_result": result.result}
