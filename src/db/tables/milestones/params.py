from pydantic import BaseModel, Field
from typing import Optional

from ..fields import FilterParam
from ..query_params import QueryParams


class MilestoneParams(QueryParams):
    name: Optional[str] = FilterParam(
        default=None, where_clause="milestones.name = ?"
    )
    search: Optional[str] = FilterParam(
        default=None,
        where_clause='(milestones.name LIKE "%?%" OR milestones.description LIKE "%?%")',
        repeat_arg=2,
    )
    ticket_id: Optional[int] = FilterParam(
        default=None,
        where_clause="milestones.id in (SELECT milestone_id FROM ticket_milestones WHERE ticket_id = ?)",
    )
    page_number: Optional[int] = Field(1, ge=1)
    page_size: Optional[int] = Field(10, ge=1, le=100)
