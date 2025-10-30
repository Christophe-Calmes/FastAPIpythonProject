from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship

class Account(Base):
    __tablename__="accounts"
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String(60), unique=True, index=True)
    solde = Column(Float, default=0.00)
    client_id = Column(Integer, ForeignKey("clients.id"))
    owner = relationship("Client", back_populates="accounts")

