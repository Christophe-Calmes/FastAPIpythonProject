from sqlalchemy.orm import Session
from models.client import Client

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def get_client_by_email(db: Session, email: str):
    return db.query(Client).filter(Client.email == email).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Client).offset(skip).limit(limit).all()

def create_client(db: Session, nom: str, email: str):
    db_client = Client(nom=nom, email=email)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client