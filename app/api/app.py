from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
import dotenv
from api.routes import test

# Replace the placeholder with your Atlas connection string
uri = dotenv.get_key(dotenv.find_dotenv(), "MONGODB_URI")

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
async def create_item(item: Item = None):
    db = get_db()
    collection = db["yzt-mobil-backend"]
    if item is None:
        result = collection.insert_one({"name": "test", "price": 0.0})
    else:
        result = collection.insert_one(item.dict())
    if result.acknowledged:
        return {"id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=400, detail="Item not inserted")


app.include_router(test.router)
