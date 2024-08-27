import asyncio
import aiohttp
from random import randrange

from api.db import async_session, TicketDal
from api.mappers import map_ticket
from api.models.ticket import TicketModel


OUT_OF_TIME_PERIOD = 15
UPDATE_STATUS_PERIOD = 50
CLIENT_URL = 'http://localhost:3000/tickets/outdated'


async def send_out_of_time_tickets():
    while True:
        async with async_session() as session:
            async with session.begin():
                ticket_dal = TicketDal(session)
                outdated_tickets = await ticket_dal.get_outdated_tickets()
        await make_client_request(tickets=outdated_tickets)
        await asyncio.sleep(OUT_OF_TIME_PERIOD)


async def change_ticket_statuses():
    while True:
        async with async_session() as session:
            async with session.begin():
                ticket_dal = TicketDal(session)
                quantity = randrange(1, 4)
                updated_tickets = await ticket_dal.update_ticket_statuses(quantity=quantity)
        await make_client_request(tickets=updated_tickets)
        await asyncio.sleep(UPDATE_STATUS_PERIOD)


async def make_client_request(tickets: TicketModel):
    body = map_ticket(tickets)
    if len(body.tickets):
        async with aiohttp.ClientSession() as session:
            response = session.post(CLIENT_URL, data=body)
            # TODO: some response processing


async def run_tasks():
    task1 = asyncio.create_task(send_out_of_time_tickets())
    task2 = asyncio.create_task(change_ticket_statuses())
    await asyncio.gather(task1, task2)
