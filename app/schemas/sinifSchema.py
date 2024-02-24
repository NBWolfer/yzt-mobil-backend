from pydantic import BaseModel
from . import usageSchema

class SinifBase(BaseModel):
    faculty: str
    building: str
    floor: str

class Sinif(SinifBase):
    id: int
    usages: list[usageSchema.UsageSchema] = []

    class Config:
        from_attributes = True


class SinifCreate(SinifBase):
    pass