from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(60), index=True)
    email = Column(String(70), unique=True, index=True)
    date_inscription = Column(DateTime(timezone=True), server_default=func.now())
    accounts = relationship("Account", back_populates="owner")