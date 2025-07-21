from fastapi import FastAPI, HTTPException, Depends
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

@app.post("/api/forms/wheel-specifications")
def create_wheel_specification(
    formNumber: str,
    submittedBy: str,
    submittedDate: str,
    condemningDia: str,
    lastShopIssueSize: str,
    treadDiameterNew: str,
    wheelGauge: str,
    db: Session = Depends(get_db)
):
    spec = models.WheelSpecification(
        formNumber=formNumber,
        submittedBy=submittedBy,
        submittedDate=submittedDate,
        condemningDia=condemningDia,
        lastShopIssueSize=lastShopIssueSize,
        treadDiameterNew=treadDiameterNew,
        wheelGauge=wheelGauge
    )
    db.add(spec)
    db.commit()
    db.refresh(spec)
    return {"success": True, "message": "Wheel specification submitted successfully.", "data": {
        "formNumber": spec.formNumber,
        "status": "Saved",
        "submittedBy": spec.submittedBy,
        "submittedDate": spec.submittedDate
    }}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
