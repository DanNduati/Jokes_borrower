import os
from os.path import join

from dotenv import load_dotenv
from tortoise import Tortoise, run_async

from . import models

path = os.getcwd()
dotenv_path: str = join(path, ".env")
load_dotenv(dotenv_path, override=True)
database_url: str = os.environ.get("DATABASE_URL")
TORTOISE_ORM = {
    "connections": {"default": database_url},
    "apps": {
        "models": {
            "models": [models, "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init():
    await Tortoise.init(db_url=database_url, modules={"models": [models]})
    # Generate the schema
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    run_async(init())
