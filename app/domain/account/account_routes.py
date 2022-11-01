
import logging
from fastapi import HTTPException
from fastapi.routing import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Optional, List

from config import database
from domain.account import account_service
from domain.account.account_schema import AccountCreateSchema, AccountSchema

accounts = []

router = APIRouter()


@router.get("/", response_model=List[AccountSchema], summary="Return all accounts", description="Return all accounts")
def get_accounts(db: Session = Depends(database.get_db)):

    return account_service.get_accounts(db)


@router.get("/{id}", response_model=AccountSchema)
def account_id(id: int) -> Optional[AccountSchema]:

    for account in accounts:
        if (account.id == id):
            return account

    raise HTTPException(status_code=404, detail="No content")


@router.post("/", response_model=bool)
def account(account: AccountCreateSchema, db: Session = Depends(database.get_db)) -> bool:
    try:
        account_service.create(db, account)
    except Exception as e:
        logging.error(f"Error in load account: {e}", e)
        raise HTTPException(
            detail=f"Error in load account: {e}", status_code=500)
    return True
