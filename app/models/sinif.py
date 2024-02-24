from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base

class Sinif(Base):
    __tablename__ = "sinif"

    id = Column(Integer, primary_key=True, index=True)
    faculty = Column(String, index=True)
    building = Column(String, index=True)
    floor = Column(String, index=True)
    usage = relationship("Usage", back_populates="sinif")
    lesson = relationship("Lesson", back_populates="sinif")