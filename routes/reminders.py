from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Reminder, User, Invoice
from schemas import ReminderCreate, ReminderResponse, ReminderCreateResponse

router = APIRouter(prefix="/reminders", tags=["Reminders"])

@router.post("/reminders/create", response_model=ReminderCreateResponse)
def create_reminder(
    user_id: int,
    invoice_id: int,
    reminder_type: str = "email",
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    reminder = Reminder(
        user_id=user_id,
        invoice_id=invoice_id,
        reminder_type=reminder_type,
        status="sent"
    )

    db.add(reminder)
    db.commit()
    db.refresh(reminder)

    return {
        "id": reminder.id,
        "reminder_type": reminder.reminder_type,
        "status": reminder.status,
        "sent_at": reminder.sent_at,

        "user_id": user.id,
        "user_email": user.email,

        "invoice_id": invoice.id,
        "invoice_number": invoice.invoice_number
    }


@router.get("/user/{user_id}/reminders", response_model=list[ReminderResponse])
def get_user_reminders(user_id: int, db: Session = Depends(get_db)):
    return db.query(Reminder).filter(Reminder.user_id == user_id)\
        .order_by(Reminder.sent_at.desc()).all()

@router.get("/admin/reminders", response_model=list[ReminderResponse])
def get_all_reminders(db: Session = Depends(get_db)):
    return db.query(Reminder).order_by(Reminder.sent_at.desc()).all()
