from fastapi import FastAPI
from models import Job
from fake_db import get_all_jobs, add_job

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Tracker API"}

@app.get("/jobs/")
def get_jobs():
    return get_all_jobs()

@app.post("/jobs/")
def create_job(job: Job):
    return add_job(job)
