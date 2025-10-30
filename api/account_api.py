from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from schemas.accounts import AccountBase
from dependencies.dependencies import get_db
from crud.account import *


account_router = APIRouter(prefix="/accounts", tags=["accounts"])


@account_router.post("/", response_model=AccountBase, status_code=201)
def create_account_route(numero: str, solde: float, client_id: int,  db: Session = Depends(get_db)):
    return create_account(db=db,  
        numero=numero,
        solde=solde,
        client_id=client_id
        )

'''
@account_router.get("/", response_model=List[AccountBase])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_accounts(db, skip=skip, limit=limit)

@account_router.get("/{account_id}", response_model=AccountBase)
def get_account(account_id: int, db: Session = Depends(get_db)):
    db_account = get_account(db, account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Compte non trouvé")
    return db_account
'''