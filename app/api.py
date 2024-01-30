from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient

# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://enes__:WFDjPW0tqyOYvovZ@clusternbw.z4bdewm.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
def get_db():
    client = MongoClient(uri)
    db = client['yzt-mobil-app']
    return db

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"Hello": "World-2"}

class Item(BaseModel):
    name: str
    price: float

@app.post("/create/", tags=["createItem"])
async def create_item(item: Item):
    db = get_db()
    collection = db["yzt-mobil-backend"]
    result = collection.insert_one(item.dict())
    if result.acknowledged:
        return {"id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=400, detail="Item not inserted")
