from typing import Literal, Optional

from pydantic import BaseModel, Field


class ThingParams(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    parent_id: Optional[int] = Field(
        default=None,
        description="Filter by parent thing ID, 0 for top level things",
        ge=0,
    )
    search: Optional[str] = None
    include: list[Literal["category", "parent", "children"]] = []
    page_number: Optional[int] = Field(default=1, ge=1)
    page_size: Optional[int] = Field(default=10, ge=1, le=1000)
