from typing import Optional

from ..table_model import TableModel
from ..fields import (
    ColumnField,
    PrimaryKeyField,
)


class Schedule(TableModel):
    id: Optional[int] = PrimaryKeyField(None)
    name: Optional[str] = ColumnField(None)
    weekdays: Optional[str] = ColumnField(None)
    monthdays: Optional[str] = ColumnField(None)
    yeardays: Optional[str] = ColumnField(None)

    class Config:
        from_attributes = True
