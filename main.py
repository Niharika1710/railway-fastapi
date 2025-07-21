from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import engine, SessionLocal
from pydantic import BaseModel
from typing import Dict

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Schema for Request Body
class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: Dict[str, str]

@app.post("/api/forms/wheel-specifications")
def create_wheel_specification(data: WheelSpecificationCreate, db: Session = Depends(get_db)):
    db_item = models.WheelSpecification(
        formNumber=data.formNumber,
        submittedBy=data.submittedBy,
        submittedDate=data.submittedDate,
        fields=data.fields
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": db_item.formNumber,
            "submittedBy": db_item.submittedBy,
            "submittedDate": db_item.submittedDate,
            "status": "Saved"
        }
    }

# Health check (optional)
@app.get("/")
def read_root():
    return {"message": "API is live for wheel specifications"}
