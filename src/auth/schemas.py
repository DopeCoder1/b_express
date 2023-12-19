from pydantic import BaseModel, EmailStr
from pydantic import EmailStr, Field, field_validator

class UserSchemas(BaseModel):
    email: EmailStr
    password: str

    