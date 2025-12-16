from pydantic import BaseModel, Field
from typing import Optional

from ...core import QueryParams, FilterParam


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
    due_date_before: Optional[str] = FilterParam(
        default=None, where_clause="milestones.due_date < ?"
    )
    due_date_after: Optional[str] = FilterParam(
        default=None, where_clause="milestones.due_date > ?"
    )
    page_number: Optional[int] = Field(1, ge=1)
    page_size: Optional[int] = Field(10, ge=1, le=100)
