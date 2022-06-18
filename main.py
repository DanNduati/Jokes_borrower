import argparse
import asyncio
import logging
import os
import time

from jokesborrower import JokesBorrower, db

logging.basicConfig(
    filename="borrower.log",
    level=logging.INFO,
    format="%(name)s - %(asctime)s - %(levelname)s - %(message)s",
)

# Create the parser
count_parser = argparse.ArgumentParser(description="Jokesborrower id count")

# Add arguments to the parser
count_parser.add_argument(
    "Joke_index", metavar="joke index", type=int, help="The jokes index to start from"
)
# Execute the parse_args() method
args = count_parser.parse_args()
start_id: int = args.Joke_index


async def main():
    start_time = time.time()
    await db.init()
    jk = JokesBorrower(
        url="https://v2.jokeapi.dev/joke/", jokes_count=100, start_id=start_id
    )
    jokes_num: int = await jk.borrow_jokes()
    print(
        f"{jokes_num} jokes borrowed successfully in {(time.time() - start_time)} seconds"
    )
    logging.info(
        f"{jokes_num} jokes borrowed successfully in {(time.time() - start_time)} seconds"
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        os._exit(0)
