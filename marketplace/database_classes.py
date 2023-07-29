from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the database engine (replace 'sqlite:///example.db' with your database URI)
engine = create_engine('sqlite:///example.db', echo=True)

# Create a base class for our ORM models
Base = declarative_base()

# Define the ORM model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    birthdate = Column(Date)

# Create the table in the database (if it doesn't exist)
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example usage: adding a new user to the database
new_user = User(username='john_doe', email='john@example.com', birthdate='1990-01-01')
session.add(new_user)
session.commit()

# Querying the database
user = session.query(User).filter_by(username='john_doe').first()
print(user.email)

# Don't forget to close the session when you're done
session.close()
