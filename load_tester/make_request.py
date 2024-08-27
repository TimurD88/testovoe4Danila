import asyncio
import datetime
import uuid
from time import sleep

import aiohttp
from datetime import datetime, timedelta
from random import randrange, choice
import os
import requests

REQUESTS_DELAY = int(os.environ['requests_delay'])
CLIENT_URL = 'http://localhost:8000/api/ticket'


def generate_request() -> dict[str, str]:
    body = {
        "source_system": "imitation",
        "name": str(uuid.uuid4())[:8],
        "status": choice(("new", "waiting response", "solved")),
        "timeToSolve": str(datetime.now() + timedelta(minutes=randrange(1, 250)))
    }
    return body


def make_api_request(body) -> None:
    requests.post(CLIENT_URL, json=body)
    sleep(randrange(REQUESTS_DELAY, 2 * REQUESTS_DELAY)/1000)
