
from datetime import date
from pydantic import BaseModel, Field
from typing import Optional


class AccountSchema(BaseModel):
    id: int
    name: str = Field(..., example="João")
    document: str
    born_date: date
    email: str
    phone_number: Optional[str]

    class Config:
        orm_mode = True


class AccountCreateSchema(BaseModel):
    name: str = Field(..., example="João")
    document: str
    born_date: date
    email: str
    phone_number: Optional[str]

    class Config:
        orm_mode = True