from os import environ
from app import meta

# environ.load(APP_NAME=meta.__title__, APP_VERSION=meta.__version__)

# DEBUG = environ.debug()

APP_DEBUG: bool = environ.get("APP_DEBUG", default=False)

DATABASE_URL: str = environ.get(
    "DATABASE_URL", default="postgresql://postgres:postgres@localhost:5432/investment")

SECRET_KEY: str = environ.get(
    "SECRET_KEY", default="secret"
)