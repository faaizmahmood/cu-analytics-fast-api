from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite Database Configuration (No need for an actual DB server)
DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Example Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Create the tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Insert and fetch dummy data
def test_db():
    db = SessionLocal()
    # Insert a user
    new_user = User(name="John Doe")
    db.add(new_user)
    db.commit()
    
    # Fetch users
    users = db.query(User).all()
    for user in users:
        print(f"User ID: {user.id}, Name: {user.name}")
    
    db.close()

if __name__ == "__main__":
    test_db()
