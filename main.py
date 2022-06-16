import asyncio
import logging
import time
import os

from jokesborrower import JokesBorrower, db

logging.basicConfig(
    filename="borrower.log",
    level=logging.INFO,
    format="%(name)s - %(asctime)s - %(levelname)s - %(message)s",
)


async def main():
    start_time = time.time()
    await db.init()
    jk = JokesBorrower(
        url="https://v2.jokeapi.dev/joke/",
        jokes_count=100,
    )
    await jk.borrow_jokes()
    print(F"100 jokes borrowed successfully in {(time.time() - start_time)} seconds")
    logging.info(F"100 jokes borrowed successfully in {(time.time() - start_time)} seconds")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        os._exit(0)