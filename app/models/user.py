from sqlalchemy import Column, Integer, String
from ..db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    __table_args__ = {"extend_existing": True}  # Add this line
