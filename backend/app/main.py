from typing import Union

from fastapi import FastAPI
from app.api.endpoints.upload import router as upload_router

app = FastAPI()

app.include_router(upload_router, prefix="/upload")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
