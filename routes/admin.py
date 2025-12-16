from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User,Invoice
from schemas import UserResponse,InvoiceResponse
from sqlalchemy.orm import joinedload


router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/invoices", response_model=list[InvoiceResponse])
def get_all_invoices(db: Session = Depends(get_db)):
    invoices = (
        db.query(Invoice)
        .options(joinedload(Invoice.user))
        .all()
    )
    return invoices
