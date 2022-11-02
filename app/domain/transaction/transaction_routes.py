from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from domain.transaction.transaction_schema import TransactionSchema, TransactionCreationSchema
from domain.transaction import transaction_service
from config import database

router = APIRouter()


@router.post("/")
def create_transction(transaction: TransactionCreationSchema, db: Session = Depends(database.get_db)):
    transaction_service.create_transaction(transaction, db)
