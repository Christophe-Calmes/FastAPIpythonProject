from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from schemas.clients import *
from crud.client import *
from dependencies.dependencies import get_db

client_router = APIRouter(prefix="/clients", tags=["clients"])

@client_router.post("/")
def create_client_root(nom: str, email: str, db: Session = Depends(get_db)):
    db_client = get_client_by_email(db, email=email)
    if db_client:
        raise HTTPException(status_code=400, detail="Email déjà utilisé")
    return create_client(db=db, nom=nom, email=email)

@client_router.get("/")
def read_clients( skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_clients(db, skip=skip, limit=limit)

@client_router.get("/{client_id}")
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return db_client
@client_router.get("/email/{email}")
def read_client_by_email(email: str,  db: Session = Depends(get_db)):
    db_client = get_client_by_email(db, email=email)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return db_client
