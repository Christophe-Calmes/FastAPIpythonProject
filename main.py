from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models.client import Client
from models.account import Account
from crud.client import create_client, get_clients, get_client, get_client_by_email
# Crée les tables
Base.metadata.create_all(bind=engine)
'''
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class ClientCreate(BaseModel):
    nom: str
    email: str

@app.post(
    "/clients/",
    response_model=ClientCreate,
    status_code=status.HTTP_201_CREATED,
    summary="🆕 Créer un nouveau client",
    description="""
    Crée un client bancaire avec les informations fournies.
    
    - **nom** : doit être non vide
    - **email** : doit être unique
    
    Retourne le client créé avec son ID.
    """,
    tags=["Clients"],
    responses={
        400: {
            "description": "Email déjà utilisé",
            "content": {
                "application/json": {
                    "example": {"detail": "Email déjà utilisé"}
                }
            }
        }
    }
)
def create_client(client: ClientCreate):
    # Votre logique ici
    if client.email == "dupont@bank.com":
        raise HTTPException(status_code=400, detail="Email déjà utilisé")
    return client


'''

app = FastAPI(title="BankAPI")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clients/")
def create_client_root(nom: str, email: str, db: Session = Depends(get_db)):
    db_client = get_client_by_email(db, email=email)
    if db_client:
        raise HTTPException(status_code=400, detail="Email déjà utilisé")
    return create_client(db=db, nom=nom, email=email)

@app.get("/clients/")
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_clients(db, skip=skip, limit=limit)

@app.get("/clients/{client_id}")
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return db_client
#@app.get("/clients/email/{email}", response_model=schemas.Client)
@app.get("/clients/email/{email}")
def read_client_by_email(email: str, db: Session = Depends(get_db)):
    db_client = get_client_by_email(db, email=email)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return db_client
