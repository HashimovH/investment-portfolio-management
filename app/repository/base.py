import abc
from sqlalchemy.ext.asyncio import AsyncSession

class Repository(abc.ABC):
    def __init__(self, db_session: AsyncSession) -> None:
        self._session = db_session