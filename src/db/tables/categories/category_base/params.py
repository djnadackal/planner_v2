from typing import Optional

from ....core import QueryParams, FilterParam


class CategoryParams(QueryParams):
    name: Optional[str] = FilterParam(
        default=None, where_clause="categories.name = ?"
    )
    search: Optional[str] = FilterParam(
        default=None,
        where_clause='(categories.name LIKE "%?%" OR categories.description LIKE "%?%")',
        repeat_arg=2,
    )
