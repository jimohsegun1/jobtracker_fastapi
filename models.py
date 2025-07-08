from pydantic import BaseModel
from typing import Optional

class Job(BaseModel):
    title: str
    company: str
    location: str
    status: Optional[str] = "pending"
