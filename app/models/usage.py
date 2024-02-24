from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base

class Usage(Base):
    __tablename__ = "usage"

    id = Column(Integer, primary_key=True, index=True)
    usedBy = Column(String, index=True)
    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    lesson = relationship("Lesson", back_populates="usage")
    
    startTime = Column(String, index=True)
    endTime = Column(String, index=True)

    sinif_id = Column(Integer, ForeignKey("sinif.id"))
    sinif = relationship("Sinif", back_populates="usage")