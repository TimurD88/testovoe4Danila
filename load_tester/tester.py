import asyncio
from concurrent.futures import ThreadPoolExecutor
import os

from make_request import make_api_request, generate_request

THREADS_NUM = int(os.environ['threads_num'])


def worker():
    while True:
        req = generate_request()
        make_api_request(req)


def main():
    with ThreadPoolExecutor(max_workers=THREADS_NUM) as executor:
        futures = [executor.submit(worker) for _ in range(THREADS_NUM)]
        for future in futures:
            try:
                future.result()
            except Exception as e:
                print(f"Worker raised an exception: {e}")


if __name__ == "__main__":
    main()
