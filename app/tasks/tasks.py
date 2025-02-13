import time
from app.worker.celery import celery

@celery.task
def add_numbers(x, y):
    time.sleep(5)  # Simulate long-running task
    return x + y
