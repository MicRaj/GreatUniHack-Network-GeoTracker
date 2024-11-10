from typing import Union

from fastapi import FastAPI
from app.core.database import create_db_and_tables, SessionDep

app = FastAPI()
create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}