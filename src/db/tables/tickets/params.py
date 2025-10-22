from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import datetime
from ..util import FilterParam
from ..query_params import QueryParams


# TODO: merge thing id and thing ids, should be easy


class TicketParams(QueryParams):
    thing_ids: Optional[list[int]] = FilterParam(
        default=None, where_clause="thing_id IN ({})"
    )
    category_id: Optional[int] = FilterParam(
        default=None, where_clause="category_id = ?"
    )
    parent_id: Optional[int] = FilterParam(
        default=None, where_clause="parent_id = ?"
    )
    open: Optional[bool] = FilterParam(
        default=None, where_clause="open = ?"
    )
    search: Optional[str] = FilterParam(
        default=None,
        where_clause='(description LIKE "%?%" OR title LIKE "%?%")',
        repeat_arg=2,
    )
    created_after: Optional[datetime] = FilterParam(
        default=None, where_clause="created_at >= ?"
    )
    created_before: Optional[datetime] = FilterParam(
        default=None, where_clause="created_at <= ?"
    )
    updated_after: Optional[datetime] = FilterParam(
        default=None, where_clause="updated_at >= ?"
    )
    updated_before: Optional[datetime] = FilterParam(
        default=None, where_clause="updated_at <= ?"
    )
    completed_after: Optional[datetime] = FilterParam(
        default=None, where_clause="completed_at >= ?"
    )
    completed_before: Optional[datetime] = FilterParam(
        default=None, where_clause="completed_at <= ?"
    )
    exclude_ids: Optional[list[int]] = FilterParam(
        default=None, where_clause="id NOT IN ({})"
    )
    include: list[Literal["thing", "category", "parent", "children"]] = []
    page_number: Optional[int] = Field(1, ge=1)
    page_size: Optional[int] = Field(10, ge=1, le=100)
