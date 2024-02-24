from pydantic import BaseModel

class UsageSchema(BaseModel):
    departmentUsed: str
    startTime: str
    endTime: str
    class_ : int
