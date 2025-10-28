'''
id, numero (unique), solde (≥ 0), client_id (clé étrangère)
Ajoutez la relation bidirectionnelle :
Client.accounts → liste des comptes
Account.owner → client propriétaire
Recréez la base (bank.db).
'''
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Account(Base):
    __tablename__="accounts"
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, unique=True, index=True)
    solde = Column(float, default=0.00)
    client_id =Column(Integer, ForeignKeyy('clients.id'))
    owner = relationship("Clients", back_populates="accounts")

