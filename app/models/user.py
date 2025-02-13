from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
import bcrypt
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    provider = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @validates('password')
    def hash_password(self, key, password):
        if password:
            # Hash the password before storing
            salt = bcrypt.gensalt(rounds=10)
            return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
        return password

    def compare_password(self, candidate_password: str) -> bool:
        # Compare candidate password with the stored hashed password
        return bcrypt.checkpw(candidate_password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
