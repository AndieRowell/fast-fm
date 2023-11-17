from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

#schemas help us do defensive programming - data validation
#like the contract between frontend and backend
# - define the how the data should return back to you and EXPECT it exactly that way otherwise error
class Base(BaseModel):
    pass

class User(Base):
    id: int
    name: str
    username: str
    email: EmailStr
    password: str
    created_timestamp: datetime
