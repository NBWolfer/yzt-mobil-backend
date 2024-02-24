from sqlalchemy import Boolean, String, Integer, Column
from sqlalchemy.orm import relationship

from database.database import Base
from .lesson_lecturer import Lesson_Lecturer


class Lecturer(Base):
    __tablename__ = "lecturer"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True)
    faculty = Column(String, index=True)
    building = Column(String, index=True)
    floor = Column(String, index=True)

    lesson = relationship("Lesson", secondary="lesson_lecturer", back_populates="lecturer")