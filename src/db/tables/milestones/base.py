from typing import TYPE_CHECKING, Optional
from datetime import datetime

from ...core import ColumnField, PrimaryKeyField, TableModel


class Milestone(TableModel):
    id: Optional[int] = PrimaryKeyField(None)
    name: Optional[str] = ColumnField(None)
    description: Optional[str] = ColumnField(None)
    due_date: Optional[datetime] = ColumnField(None)
    start_date: Optional[datetime] = ColumnField(None)

    class Config:
        from_attributes = True
