from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/echo")
async def echo(mes: str = ""):
    return {"message": mes}

@app.get("/helloname")
async def echo(name: str = ""):
    return {"message": "Hello " + name}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.post("/items")
def update_item(item: Item):
    return {"item_name": item.name, "twice price": item.price * 2}
