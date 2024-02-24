from pydantic import BaseModel

class LessonBaseSchema(BaseModel):
    name : str
    code : str
    grade : str

class LessonSchema(LessonBaseSchema):
    id : int
    class Config:
        from_attributes = True

class LessonCreateSchema(LessonBaseSchema):
    pass