from pydantic import BaseModel,EmailStr
from datetime import date

# ---------- USER ----------

# ---------- REGISTER ----------
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
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
