from typing import TYPE_CHECKING, Optional, List
from datetime import datetime

from ...core import (
    ColumnField,
    DateTimeField,
    ForeignKeyField,
    RelationshipField,
    PrimaryKeyField,
    TableModel,
)

if TYPE_CHECKING:
    from ..things import Thing
    from ..categories import TicketCategory
    from ..users import User
    from ..schedules import Schedule
    from ..milestones import Milestone


# Pydantic model for Ticket
class Ticket(TableModel):
    id: Optional[int] = PrimaryKeyField(None)
    title: Optional[str] = ColumnField(None, nullable=False)
    description: Optional[str] = ColumnField(None)
    open: Optional[bool] = ColumnField(True)
    overdue: Optional[bool] = ColumnField(False)

    created_at: Optional[datetime] = DateTimeField(
        use_current_timestamp=True
    )
    updated_at: Optional[datetime] = DateTimeField(
        use_current_timestamp=True
    )
    completed_at: Optional[datetime] = DateTimeField()
    due_date: Optional[datetime] = DateTimeField()

    thing_id: Optional[int] = ForeignKeyField(None, on="id")
    category_id: Optional[int] = ForeignKeyField(None, on="id")
    parent_id: Optional[int] = ForeignKeyField(None, on="id")
    user_id: Optional[int] = ForeignKeyField(None, on="id")
    schedule_id: Optional[int] = ForeignKeyField(None, on="id")

    thing: Optional["Thing"] = RelationshipField(table_model="Thing")
    category: Optional["TicketCategory"] = RelationshipField(
        table_model="TicketCategory"
    )
    parent: Optional["Ticket"] = RelationshipField(table_model="Ticket")
    user: Optional["User"] = RelationshipField(table_model="User")
    schedule: Optional["Schedule"] = RelationshipField(
        table_model="Schedule"
    )
    children: Optional[List["Ticket"]] = None
    milestones: Optional[List["Milestone"]] = None

    class Config:
        from_attributes = True
