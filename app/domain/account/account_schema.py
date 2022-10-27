
from pydantic import BaseModel, Field
from typing import Optional


class Account(BaseModel):
    id: int
    name: str=Field(..., example="João")
    document: str
    bornDate: str
    email: str
    phoneNumber: Optional[str]