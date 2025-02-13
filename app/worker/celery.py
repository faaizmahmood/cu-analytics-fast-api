from celery import Celery

celery = Celery(
    "worker",
    broker="redis://localhost:6379/0",  # Redis for queuing tasks
    backend="redis://localhost:6379/0"  # Redis for storing results
)

celery.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_expires=3600,  # Task results expire in 1 hour
)
