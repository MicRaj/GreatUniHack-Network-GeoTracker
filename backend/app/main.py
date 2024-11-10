from typing import Union

from fastapi import FastAPI
from app.core.database import create_db_and_tables, SessionDep
from app.core.geoip import get_geo_info

app = FastAPI()
create_db_and_tables()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/ip_info/{ip}")
def ip_info(ip: str, session: SessionDep):
    return {"response": get_geo_info(ip, session)}