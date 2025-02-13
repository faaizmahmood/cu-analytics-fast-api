from sqlalchemy import Column, Integer, String
from ..db.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)  # Ensure it's defined
    hashed_password = Column(String, nullable=False)

    __table_args__ = {"extend_existing": True} 
