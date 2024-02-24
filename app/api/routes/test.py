from fastapi import APIRouter, Depends, HTTPException
import schemas
from models import Sinif
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from database.database import engine, SessionLocal, Base

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/test", tags=["test"])
async def read_test():
    print("hit test")
    return {"Hello": "Test Message"}

@router.post("/sinif/create", response_model=schemas.sinifSchema.Sinif)
async def createClass(sinif: schemas.sinifSchema.SinifCreate, db: Session = Depends(get_db)):
    print("hit /sinif/create")
    db_sinif = Sinif(faculty=sinif.faculty, building=sinif.building, floor=sinif.floor)
    db.add(db_sinif)
    db.commit()
    db.refresh(db_sinif)
    return db_sinif