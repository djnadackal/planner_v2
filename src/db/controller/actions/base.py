from datetime import datetime
from typing import TYPE_CHECKING, Optional

from pydantic import BaseModel

if TYPE_CHECKING:
    from ..tickets import Ticket
    from ..action_types import ActionType


class Action(BaseModel):
    id: Optional[int] = None
    ticket_id: Optional[int] = None
    action_text: Optional[str] = None
    action_type_id: Optional[int] = None
    performed_at: Optional[datetime] = None
    ticket: Optional["Ticket"] = None
    action_type: Optional["ActionType"] = None

    class Config:
        from_attributes = True
