from os import environ

APP_DEBUG: bool = environ.get("APP_DEBUG", default=False)

DATABASE_URL: str = environ.get(
    "DATABASE_URL", default="postgresql://postgres:postgres@localhost:5432/investment"
)

SECRET_KEY: str = environ.get("SECRET_KEY", default="secret")
