from numpy import double
from pydantic import BaseModel, Field


class TransactionSchema(BaseModel):
    id: int
    transaction_type: str
    amount: float
    account_id: str
    destination_account: str

    class Config:
        orm_mode: True


class TransactionCreationSchema(BaseModel):
    transaction_type: str = Field(..., example="pix")
    amount: float = Field(..., example=10.00)
    account_id: str = Field(..., example="2")
    destination_account: str = Field(..., example="gu@teste.com")

    class Config:
        orm_mode: True
