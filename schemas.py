from pydantic import BaseModel,EmailStr,Field
from datetime import date
from typing import Optional

# ---------- USER ----------

# ---------- REGISTER ----------
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)
    role: str = "user"


# ---------- LOGIN ----------
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ---------- RESPONSE ----------
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str 

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# ---------- INVOICE ----------

class InvoiceUser(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True


class InvoiceCreate(BaseModel):
    invoice_number: str
    customer_name: str
    amount: float
    issue_date: date
    due_date: date

class InvoiceResponse(InvoiceCreate):
    id: int
    status: str
    user_id: int
    invoice_number: str
    customer_name: str
    issue_date: date
    due_date: date
    user: InvoiceUser

    class Config:
        from_attributes = True
