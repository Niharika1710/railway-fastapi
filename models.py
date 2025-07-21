from sqlalchemy import Column, Integer, String
from database import Base

class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, index=True)
    submittedBy = Column(String)
    submittedDate = Column(String)

    treadDiameterNew = Column(String)
    lastShopIssueSize = Column(String)
    condemningDia = Column(String)
    wheelGauge = Column(String)
    variationSameAxle = Column(String)
    variationSameBogie = Column(String)
    variationSameCoach = Column(String)
    wheelProfile = Column(String)
    intermediateWWP = Column(String)
    bearingSeatDiameter = Column(String)
    rollerBearingOuterDia = Column(String)
    rollerBearingBoreDia = Column(String)
    rollerBearingWidth = Column(String)
    axleBoxHousingBoreDia = Column(String)
    wheelDiscWidth = Column(String)
