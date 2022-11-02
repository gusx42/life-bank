from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base


class Transaction(Base):

    __tablename__ = "transaction"

    id =  Column(Integer, primary_key=True, index=True)
    transaction_type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    # account_id = Column(String, nullable=False)
    destination_account = Column(String, nullable=False)
    account_id = Column(String, ForeignKey("accounts.id"))
    account = relationship("Account")
