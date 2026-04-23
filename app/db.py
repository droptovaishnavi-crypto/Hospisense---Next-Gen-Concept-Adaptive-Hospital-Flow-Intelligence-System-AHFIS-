from sqlalchemy import create_engine

# SQLite database
engine = create_engine("sqlite:///hospital.db", echo=True)