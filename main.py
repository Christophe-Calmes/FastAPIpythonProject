from fastapi import FastAPI, Depends, HTTPException
from models.client import Client
from models.account import Account
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from crud.client import create_client, get_clients, get_client, get_client_by_email
from crud.account import *
from api.account_api import account_router
from api.client_api import client_router

# Crée les tables
Base.metadata.create_all(bind=engine)
app = FastAPI(title="BankAPI")
app.include_router(account_router)
app.include_router(client_router)


