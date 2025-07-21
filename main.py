from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List
from datetime import date

from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request model
class WheelSpecificationRequest(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: Dict[str, str]

@app.post("/api/forms/wheel-specifications")
def create_wheel_specification(data: WheelSpecificationRequest, db: Session = Depends(get_db)):
    spec = models.WheelSpecification(
        formNumber=data.formNumber,
        submittedBy=data.submittedBy,
        submittedDate=data.submittedDate,
        fields=data.fields
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

@app.get("/api/forms/wheel-specifications")
def get_wheel_specifications(
    formNumber: Optional[str] = None,
    submittedBy: Optional[str] = None,
    submittedDate: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.WheelSpecification)
    if formNumber:
        query = query.filter(models.WheelSpecification.formNumber == formNumber)
    if submittedBy:
        query = query.filter(models.WheelSpecification.submittedBy == submittedBy)
    if submittedDate:
        query = query.filter(models.WheelSpecification.submittedDate == submittedDate)
    results = query.all()
    data = []
    for spec in results:
        data.append({
            "formNumber": spec.formNumber,
            "submittedBy": spec.submittedBy,
            "submittedDate": spec.submittedDate,
            "fields": spec.fields
        })
    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": data
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
