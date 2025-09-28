from pydantic import BaseModel, Field
from typing import Optional


class CommentParams(BaseModel):
    content: Optional[str] = None
    ticket_id: Optional[int] = None
    page_number: Optional[int] = Field(1, ge=1)
    page_size: Optional[int] = Field(10, ge=1, le=100)
