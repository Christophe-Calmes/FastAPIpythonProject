from sqlalchemy.orm import Session
from models.account import Account 
from schemas.accounts import AccountBase
from typing import List

# ---(GET) ---


def get_accounts(db: Session, skip: int = 0, limit: int = 100) -> List[Account]:
    """Récupère une liste de comptes avec pagination."""
    return db.query(Account).offset(skip).limit(limit).all()

def get_account_by_ID(db: Session, account_id: int) -> Account | None:
    """Récupère un seul compte par son ID."""
    return db.query(Account).filter(Account.id == account_id).first()



# ---(POST) ---
def create_account(db: Session, numero: str, solde: float, client_id: int ) -> Account:
    """Crée un nouveau compte dans la base de données."""
    
    db_account = Account(
        numero=numero,
        solde=solde,
        client_id=client_id
    )
    
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account