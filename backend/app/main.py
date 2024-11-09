from fastapi import FastAPI, Depends, HTTPException
from app.core.schemas import NetworkDataCreate, NetworkData
from app.core import crud
from app.core.database import init_db

# Initialize the database
init_db()

app = FastAPI()

# Endpoint to create a new network data entry
@app.post("/network_data/", response_model=NetworkData)
def create_network_data(data: NetworkDataCreate):
    crud.create_network_data(data)
    return data

# Endpoint to retrieve a list of network data entries
@app.get("/network_data/", response_model=list[NetworkData])
def read_network_data(skip: int = 0, limit: int = 100):
    entries = crud.get_network_data(skip=skip, limit=limit)
    return entries
