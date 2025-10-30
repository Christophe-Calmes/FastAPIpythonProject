from pydantic import BaseModel
from datetime import datetime

class ClientBase(BaseModel):
    nom: str
    email: str

class ClientCreate(ClientBase):
    pass  # mêmes champs que ClientBase, mais tu peux en ajouter si nécessaire

class ClientRead(ClientBase):
    id: int
    date_inscription: datetime
    class Config:
        orm_mode = True


