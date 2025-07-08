from models import Job

jobs = [
    Job(title="Software Engineer", company="Google", location="Mountain View, CA"),
    Job(title="Data Scientist", company="Microsoft", location="Redmond, WA", status="interviewing"),
    Job(title="Product Manager", company="Amazon", location="Seattle, WA")
]

def get_all_jobs():
    return jobs

def add_job(job):
    jobs.append(job)
    return job