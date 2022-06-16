import os
from tortoise import Tortoise,run_async
from . import models

TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": [models, "aerich.models"],
            "default_connection": "default",
        },
    },
}

async def init():
    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": [models]})
    # Generate the schema
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    run_async(init())