from fastapi import APIRouter

from api.mappers import map_ticket
from api.views import (
    TicketPost,
    Tickets, TicketPostResponse, TicketBody
)

from api.db import TicketDal, async_session

ticket_router = APIRouter(prefix='/api')


@ticket_router.post("/ticket", response_model=TicketPostResponse)
async def create_user(request: TicketPost) -> TicketPostResponse:
    async with async_session() as session:
        async with session.begin():
            ticket_dal = TicketDal(session)
            ticket = await ticket_dal.create_ticket(ticket=request)
    return TicketPostResponse(status="")


@ticket_router.get("/ticket", response_model=Tickets)
async def create_user() -> Tickets:
    async with async_session() as session:
        async with session.begin():
            ticket_dal = TicketDal(session)
            tickets = await ticket_dal.get_tickets()
            return map_ticket(tickets)
