from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for request validation
class Fields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

class WheelSpecRequest(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: Fields

@app.post("/api/forms/wheel-specifications")
def create_wheel_specification(request: WheelSpecRequest, db: Session = Depends(get_db)):
    data = request
    spec = models.WheelSpecification(
        formNumber=data.formNumber,
        submittedBy=data.submittedBy,
        submittedDate=data.submittedDate,
        treadDiameterNew=data.fields.treadDiameterNew,
        lastShopIssueSize=data.fields.lastShopIssueSize,
        condemningDia=data.fields.condemningDia,
        wheelGauge=data.fields.wheelGauge,
        variationSameAxle=data.fields.variationSameAxle,
        variationSameBogie=data.fields.variationSameBogie,
        variationSameCoach=data.fields.variationSameCoach,
        wheelProfile=data.fields.wheelProfile,
        intermediateWWP=data.fields.intermediateWWP,
        bearingSeatDiameter=data.fields.bearingSeatDiameter,
        rollerBearingOuterDia=data.fields.rollerBearingOuterDia,
        rollerBearingBoreDia=data.fields.rollerBearingBoreDia,
        rollerBearingWidth=data.fields.rollerBearingWidth,
        axleBoxHousingBoreDia=data.fields.axleBoxHousingBoreDia,
        wheelDiscWidth=data.fields.wheelDiscWidth
    )
    db.add(spec)
    db.commit()
    db.refresh(spec)
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": spec.formNumber,
            "status": "Saved",
            "submittedBy": spec.submittedBy,
            "submittedDate": spec.submittedDate
        }
    }
