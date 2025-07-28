from sqlmodel import SQLModel, create_engine

# SQLite file DB in project root
DATABASE_URL = "sqlite:///./todo.db"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create Tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

