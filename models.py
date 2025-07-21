from sqlalchemy import Column, Integer, String, JSON
from database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, nullable=False)
    submittedBy = Column(String, nullable=False)
    submittedDate = Column(String, nullable=False)
    fields = Column(JSON, nullable=False)
