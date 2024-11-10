from typing import Union
from fastapi import FastAPI
from app.api.endpoints.upload import router as upload_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(upload_router, prefix="/upload")

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


@app.get("/items/")
def read_item():
    return {"message":"Hello"}