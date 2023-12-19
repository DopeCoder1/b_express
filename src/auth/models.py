from src.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class AuthUser(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False) 
    is_active = Column(Boolean, default=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
