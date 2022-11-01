from typing import List

from domain.transaction.transaction_schema import TransactionSchema
from fastapi.routing import APIRouter


router = APIRouter()

@router.get("/", response_model=List[TransactionSchema], summary="Return all transacoes do usuario", description="Return all transactions")
def get_transction() -> List[TransactionSchema]:
    pass
    # return transactions
