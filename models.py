from sqlalchemy import Column, Integer, String, Date
from database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, index=True)
    submittedBy = Column(String)
    submittedDate = Column(String)
    condemningDia = Column(String)
    lastShopIssueSize = Column(String)
    treadDiameterNew = Column(String)
    wheelGauge = Column(String)
