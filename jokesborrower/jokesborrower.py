import asyncio
from typing import List

import aiohttp

from .models import Jokes


class JokesBorrower(object):
    def __init__(
        self,
        url: str,
        rate_limit: int = None,
        jokes_category: List = ["Any"],
        jokes_count: int = 100,
    ):
        """Constructor

        Args:
            url (str): API base url
            rate_limit (int, optional): The rate limit if any for the api. Defaults to None.
            jokes_category (List, optional): Categories of jokes you want. Defaults to ["Any"]
            jokes_count (int, optional): The number of jokes you want. Defaults to 100.
        """
        self.jokes_category = jokes_category
        self.url = (
            url + f"{','.join(self.jokes_category)}?type=twopart"
        )  # Build the jokes url by first concatenating the base url with a
        # comma-seperated string of each joke category and the type query parameter
        self.rate_limit = rate_limit  # ToDo: implement a way to throttle api requests to not exceed the rate limit
        self.jokes_count = jokes_count

        self.tasks = []
        self.jokes = []

    async def get_joke(self, session):
        async with session.get(self.url) as resp:
            joke = await resp.json()
            return joke

    async def get_jokes(self):
        async with aiohttp.ClientSession() as session:
            for i in range(self.jokes_count):
                self.tasks.append(asyncio.ensure_future(self.get_joke(session)))
            self.jokes = await asyncio.gather(*self.tasks)
        return self.jokes

    async def store_jokes(self, jokes):
        self._jokes = jokes
        for joke in self._jokes:
            await Jokes.create(
                setup=joke["setup"], punchline=joke["punchline"], type=joke["type"]
            )

    def reshape_response(self, resp: dict):
        self.data = resp
        # remove unnecessary fields
        for element in ["error", "flags", "safe", "id", "lang", "type"]:
            self.data.pop(element)
        # rename category and delivery key to type and punchline respectively
        self.data["type"] = self.data.pop("category")
        self.data["punchline"] = self.data.pop("delivery")

    async def borrow_jokes(self):
        jokes_list = await self.get_jokes()
        # Cleanup the jokes list returning only fields needed -> ["category","setup","delivery(punchline)"]
        for joke in jokes_list:
            self.reshape_response(joke)
        # store the jokes to the database
        await self.store_jokes(jokes_list)
