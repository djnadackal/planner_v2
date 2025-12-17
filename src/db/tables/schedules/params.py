from pydantic import Field
from typing import Optional

from ...core import QueryParams, FilterParam


class ScheduleParams(QueryParams):
    name: Optional[str] = FilterParam(
        default=None, where_clause="schedules.name = ?"
    )
    search: Optional[str] = FilterParam(
        default=None,
        where_clause='schedules.name LIKE "%?%")',
        repeat_arg=2,
    )
    page_number: Optional[int] = Field(1, ge=1)
    page_size: Optional[int] = Field(10, ge=1, le=10000)
