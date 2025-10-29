from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from schemas import account as schemas_account

account_router = APIRouter(prefix="/accounts", tags=["accounts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas_account.Account, status_code=201)
def create_account(account: schemas_account.AccountCreate, db: Session = Depends(get_db)):
    return crud_account.create_account(db=db, account=account)

@router.get("/", response_model=List[schemas_account.Account])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_account.get_accounts(db, skip=skip, limit=limit)

@router.get("/{account_id}", response_model=schemas_account.Account)
def read_account(account_id: int, db: Session = Depends(get_db)):
    db_account = crud_account.get_account(db, account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Compte non trouvé")
    return db_account
