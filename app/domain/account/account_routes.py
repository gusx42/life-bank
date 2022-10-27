from fastapi import Response, HTTPException
from fastapi.routing import APIRouter
from typing import Optional, List

from domain.account.account_schema import Account

accounts = []

router = APIRouter()


@router.get("/", response_model=List[Account], summary="Return all accounts", description="Return all accounts")
def get_accounts() -> List[Account]:

    return accounts


@router.get("/{id}", response_model=Account)
def account_id(id: int) -> Optional[Account]:

    for account in accounts:
        if (account.id == id):
            return account

    raise HTTPException(status_code=404, detail="No content")


@router.post("/", response_model=bool)
def account(account: Account) -> bool:
    try:
        accounts.append(account)
    except Exception as e:
        print(f"Error in load account: {e}")
        return False
    return True
