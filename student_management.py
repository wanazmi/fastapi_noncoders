from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="User Management API (In-Memory)",
    description="A simple API to manage user data  CRUD operations using an in-memory list.",
    version="0.1.0",
)

# Data model
class User(BaseModel):
    name: str
    email: str
    age: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

# Fake database
users_db = []
next_id = 1
