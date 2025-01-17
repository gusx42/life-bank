import json
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from domain.account.account_model import Account
from domain.transaction.transaction_model import Transaction
from domain.transaction.transaction_repository import TransactionRepository
from domain.transaction.transaction_schema import TransactionSchema, TransactionSchemaCreate


def create(db: Session, body: TransactionSchemaCreate) -> TransactionSchema:
    account_id = int(body.account_id)
    account = TransactionRepository().filter_by_id(db, Account, account_id)
    if not account:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Deve existir uma conta para criar a transação")
    
        # if (account is not None):
    #     _account = {"name": account.name,
    #                 "document": account.document, "email": account.email}
    #     body.account = json.dumps(_account)
    transaction = Transaction(**body.dict())
    print(transaction)
    return TransactionRepository().create(db, transaction)


def get_transactions(db: Session) -> TransactionSchema:
    return TransactionRepository().all(db, Transaction)
