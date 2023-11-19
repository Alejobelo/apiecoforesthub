from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class QueryModel(BaseModel):
    query: str
    description: str
    created_at: datetime = None


