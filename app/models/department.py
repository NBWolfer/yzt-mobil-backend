from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base
from .lesson_department import Lesson_Department

class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True)
    faculty = Column(String, index=True)

    lesson = relationship("Lesson", secondary="lesson_department", back_populates="departments")

