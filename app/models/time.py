import datetime
import uuid
from sqlalchemy import Column, Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Time(Base):
    __tablename__ = "times"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(Date, nullable=False)  # Stores the date only
    entry_time = Column(DateTime, nullable=True)  # Stores the datetime of entry
    lunch_entry_time = Column(DateTime, nullable=True)  # Stores the datetime for lunch entry
    lunch_exit_time = Column(DateTime, nullable=True)  # Stores the datetime for lunch exit
    exit_time = Column(DateTime, nullable=True)  # Stores the datetime of exit

    
    def __init__(self, date: datetime.date, entry_time: datetime.datetime = None, 
                 lunch_entry_time: datetime.datetime = None, lunch_exit_time: datetime.datetime = None, 
                 exit_time: datetime.datetime = None):
        self.date = date
        self.entry_time = entry_time
        self.lunch_entry_time = lunch_entry_time
        self.lunch_exit_time = lunch_exit_time
        self.exit_time = exit_time
    
    def set_current_times(self):
        """ Set current time for all time fields """
        now = datetime.datetime.now()
        self.entry_time = now
        self.lunch_entry_time = now
        self.lunch_exit_time = now
        self.exit_time = now
