from typing import Union
from fastapi import FastAPI
from app.core.database import create_db_and_tables, SessionDep
from app.core.geoip import get_geo_info
from app.api.endpoints.upload import router as upload_router
from app.api.endpoints.data import router as data_router
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(upload_router)
app.include_router(data_router)

# Allowing CORS from the specific origin (localhost:5173) or any origin
origins = [
    "http://localhost:5173",  # Frontend app URL
    "http://127.0.0.1:5173",  # Or you can use localhost and 127.0.0.1 as the origin
]

# Adding CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins or "*" for all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # List allowed methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ip_info/{ip}")
def ip_info(ip: str, session: SessionDep):
    return {"response": get_geo_info(ip, session)}

@app.get("/items/")
def read_item():
    return {"message":"Hello"}

