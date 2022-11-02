

from sqlalchemy.orm.session import Session

from ..account.account_repository import AccountRepository
from ..account.account_schema import AccountCreateSchema, AccountSchema
from ..account import account_model


def create(db: Session, account: AccountCreateSchema) -> AccountSchema:
    # account = AccountCreateSchema
    
    account_item = account_model.Account(**account.dict())
    
    return AccountRepository().create(db, account_item)


def get_accounts(db: Session) -> AccountSchema:
    # return db.query(account_model.Account).all()
    result = AccountRepository().all(db, account_model.Account)

    print(result)
    
    return result
    # return AccountRepository().all(db, account_model.Account)
