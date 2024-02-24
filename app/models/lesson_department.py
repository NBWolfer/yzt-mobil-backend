from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


class Lesson_Department(Base):
    __tablename__ = "lesson_department"

    id = Column(Integer, primary_key=True, index=True)

    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    
    department_id = Column(Integer, ForeignKey("department.id"))