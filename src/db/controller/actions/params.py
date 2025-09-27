from typing import Literal, Optional

from pydantic import BaseModel, Field


class ActionParams(BaseModel):
    action_type: Optional[str] = None
    ticket_id: Optional[int] = None
    include: list[Literal["ticket", "action_type"]] = []
    page_number: Optional[int] = Field(1, ge=1)
    page_size: Optional[int] = Field(10, ge=1, le=100)
