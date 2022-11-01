from typing import Optional
from pydantic import BaseModel


class TransactionSchema(BaseModel):
    id: int
    account_id: int
    value: int
