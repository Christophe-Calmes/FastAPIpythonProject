from database import Base, engine
from models.client import Client
from models.account import Account

print("Tentative de création des tables...")
Base.metadata.create_all(bind=engine)
print("Création terminée. Vérifiez le fichier bank.db.")