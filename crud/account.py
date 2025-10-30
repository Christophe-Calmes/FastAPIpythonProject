from sqlalchemy.orm import Session
from models.account import Account 
from schemas.accounts import AccountBase
from typing import List

# ---(GET) ---

def get_account(db: Session, account_id: int) -> Account | None:
    """Récupère un seul compte par son ID."""
    return db.query(Account).filter(Account.id == account_id).first()

def get_accounts(db: Session, skip: int = 0, limit: int = 100) -> List[Account]:
    """Récupère une liste de comptes avec pagination."""
    return db.query(Account).offset(skip).limit(limit).all()
# ---(POST) ---
def create_account(
    db: Session, 
    account_data: AccountBase 
) -> Account:
    """Crée un nouveau compte dans la base de données."""
    
    # Crée une instance du modèle SQLAlchemy en utilisant les données Pydantic
    db_account = Account(
        numero=account_data.numero,
        solde=account_data.solde,
        client_id=account_data.client_id
    )
    
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account