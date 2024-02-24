from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import dotenv
from api.routes import test
from database.database import engine, SessionLocal, Base
from models import Sinif
from schemas import sinifSchema

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/home", tags=["Root"])
async def read_root():
    return {"Hello": "World-2"}

app.include_router(test.router)
