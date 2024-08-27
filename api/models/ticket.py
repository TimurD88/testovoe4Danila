from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID

import uuid

Base = declarative_base()


class TicketModel(Base):
    __tablename__ = 'tickets'
    ticket_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source_system = Column(String)
    name = Column(String)
    status = Column(String)
    timeToSolve = Column(DateTime)
    timeCreate = Column(DateTime)
