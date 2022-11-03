from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from domain.account.account_schema import AccountSchema


class TransactionSchema(BaseModel):
    id: int
    transaction_type: str
    amount: float
    account: Optional[AccountSchema]
    destination_account: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class TransactionSchemaCreate(BaseModel):
    transaction_type: str=Field(..., example="pix")
    amount: float=Field(..., example=40.12)
    account_id: int=Field(..., example=2)
    destination_account: str=Field(..., example="will@net")

    class Config:
        orm_mode = True    
