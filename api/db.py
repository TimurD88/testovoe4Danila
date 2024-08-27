import datetime
import uuid

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from sqlalchemy import select, text

from api.models.ticket import TicketModel

DATABASE_URL = 'postgresql+asyncpg://postgres:postgres@localhost:5432/postgres'

engine = create_async_engine(
    DATABASE_URL,
    future=True,
    echo=True
)
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class TicketDal:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_ticket(self, ticket):
        new_ticket = TicketModel(
            source_system=ticket.source_system,
            name=ticket.name,
            status=ticket.status,
            timeToSolve=ticket.timeToSolve,  # TODO: Подумать, что тут использовать
            timeCreate=datetime.datetime.now(),
        )
        self.db_session.add(new_ticket)
        await self.db_session.flush()

    async def get_tickets(self) -> TicketModel:
        query = select(TicketModel)
        return await self.db_session.execute(query)

    async def get_outdated_tickets(self) -> TicketModel:
        query = select(TicketModel).where(
            TicketModel.timeToSolve <= datetime.datetime.now(),
            TicketModel.source_system == 'client'
        )
        return await self.db_session.execute(query)

    async def update_ticket_statuses(self, quantity: int):
        select_query = select(TicketModel).where(
            TicketModel.status == 'new',
            TicketModel.source_system == 'client'
        ).limit(quantity).with_for_update()
        results = await self.db_session.execute(select_query)
        tickets = results.scalars().all()
        if tickets:
            for ticket in tickets:
                ticket.status = 'waiting response'
        await self.db_session.commit()

        return results
