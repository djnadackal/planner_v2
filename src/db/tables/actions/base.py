from datetime import datetime
from typing import TYPE_CHECKING, Optional

from ..table_model import TableModel

if TYPE_CHECKING:
    from ..tickets import Ticket
    from ..categories import ActionType


class Action(TableModel):
    id: Optional[int] = None
    ticket_id: Optional[int] = None
    action_text: Optional[str] = None
    action_type_id: Optional[int] = None
    performed_at: Optional[datetime] = None
    ticket: Optional["Ticket"] = None
    action_type: Optional["ActionType"] = None

    class Config:
        from_attributes = True
