import asyncio
import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from api.handlers import ticket_router

from coroutines.tasks import run_tasks

app = FastAPI(title="Aboba")
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

main_api_router = APIRouter()

main_api_router.include_router(ticket_router, tags=["ticket"])
app.include_router(main_api_router)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(run_tasks())


def start_server():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
