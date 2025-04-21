import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./project.db"

#engine for database
engine = create_engine(DATABASE_URL, echo=True)

#sessionmaker for making a session for a db, no autosaving, session connected with the engine - used to communicate with a db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#base class for the rest of the models
Base = declarative_base()

