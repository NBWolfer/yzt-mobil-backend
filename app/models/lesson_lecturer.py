from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base

class Lesson_Lecturer(Base):
    __tablename__ = "lesson_lecturer"

    id = Column(Integer, primary_key=True, index=True)

    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    lecturer_id = Column(Integer, ForeignKey("lecturer.id"))