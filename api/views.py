import datetime
import uuid

from pydantic import BaseModel


class TicketPost(BaseModel):
    source_system: str
    name: str
    status: str
    timeToSolve: datetime.datetime


class TicketBody(BaseModel):
    source_system: str
    name: str
    status: str
    timeCreate: datetime.datetime
    timeToResolve: datetime.datetime


class Tickets(BaseModel):
    tickets: list[TicketBody]


class TicketPostResponse(BaseModel):
    status: str
