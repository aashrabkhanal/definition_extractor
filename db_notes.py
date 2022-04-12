import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# orm
Base = declarative_base()
engine = create_engine('sqlite:///notes.db', echo=False)
Session = sessionmaker()


class Note(Base):
    __tablename__ = "note"
    id = Column(Integer, primary_key=True, nullable=False)
    note_title = Column(String(250), nullable=False)
    note_content = Column(String(5000), nullable=False)
    date = Column(DateTime(), default=datetime.datetime.utcnow())
