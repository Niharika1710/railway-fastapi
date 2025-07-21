from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import Optional
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

@app.get("/api/forms/wheel-specifications")
def get_wheel_specifications(
    formNumber: Optional[str] = Query(None),
    submittedBy: Optional[str] = Query(None),
    submittedDate: Optional[str] = Query(None),
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
    for item in results:
        data.append({
            "formNumber": item.formNumber,
            "submittedBy": item.submittedBy,
            "submittedDate": item.submittedDate,
            "fields": item.fields
        })

    return {
        "success": True,
        "message": "Filtered wheel specification forms fetched successfully.",
        "data": data
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
