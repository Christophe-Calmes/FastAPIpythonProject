from pydantic import BaseModel
from typing import Optional

class AccountBase(BaseModel):
    numero: str
    solde: float = 0.0
    client_id: int

class AccountCreate(AccountBase):
    pass  # identique à AccountBase, mais utile si tu veux ajouter des champs de création spécifiques plus tard

class AccountRead(AccountBase):
    id: int

    class Config:
        orm_mode = True
