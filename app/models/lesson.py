from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base
from .lesson_department import Lesson_Department
from .lesson_lecturer import Lesson_Lecturer

class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(String, index=True)
    grade = Column(String, index=True)
    credit = Column(String, index=True)
    lang = Column(String, index=True)
    
    lecturer = relationship("Lecturer", secondary="lesson_lecturer", back_populates="lesson") 

    connectedCourse_id = Column(Integer, ForeignKey("lesson.id"), nullable=True)
    connectedCourse = relationship("Lesson", back_populates="courseItConnects", foreign_keys=[connectedCourse_id], remote_side=[id])

    
    courseItConnects_id = Column(Integer, ForeignKey("lesson.id"), nullable=True)
    courseItConnects = relationship("Lesson", back_populates="connectedCourse", foreign_keys=[courseItConnects_id])

    sinif_id = Column(Integer, ForeignKey("sinif.id"))
    sinif = relationship("Sinif", back_populates="lesson")

    departments = relationship("Department", secondary="lesson_department", back_populates="lesson")

    usage = relationship("Usage", back_populates="lesson")

