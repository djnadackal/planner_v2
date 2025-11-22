from typing import Optional

from ..table_model import TableModel
from ..fields import (
    ColumnField,
    PrimaryKeyField,
)


class User(TableModel):
    id: Optional[int] = PrimaryKeyField(None)
    username: Optional[str] = ColumnField(None)

    ticket_count: Optional[int] = None

    class Config:
        from_attributes = True
