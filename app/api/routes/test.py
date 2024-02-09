from fastapi import APIRouter, HTTPException


router = APIRouter()

@router.get("/test", tags=["test"])
async def read_test():
    return {"Hello": "Test Message"}
