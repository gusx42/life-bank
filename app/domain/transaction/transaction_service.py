from requests import Session
from domain.transaction.transaction_schema import TransactionSchema, TransactionCreationSchema
from domain.transaction.transaction_model import Transaction
from domain.transaction.transaction_repository import TransactionRepository


def create_transaction(transaction: TransactionCreationSchema, db: Session):
    transaction_item = Transaction(**transaction.dict())
    return TransactionRepository().create(db, transaction_item)