from typing import List

from api.models.ticket import TicketModel
from api.views import Tickets, TicketBody


def map_ticket(tickets: TicketModel) -> Tickets:
    return Tickets(
        tickets=[TicketBody(source_system=ticket.source_system,
                            name=ticket.name,
                            status=ticket.status,
                            timeCreate=ticket.timeCreate,
                            timeToResolve=ticket.timeToSolve)
                 for ticket in tickets.scalars()]
    )
