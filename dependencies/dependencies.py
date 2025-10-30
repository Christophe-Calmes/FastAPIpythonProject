from database import SessionLocal
from sqlalchemy.orm import Session # Assurez-vous d'importer Session

def get_db():
    db: Session = SessionLocal() 
    try:
        yield db
    finally:
        db.close()