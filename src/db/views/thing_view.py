from typing import Optional

from fastapi import Query

from ..controller import Thing, ThingFilter
from ..core import Database


class ThingView(Thing):
    category_name: Optional[str] = None


class ThingViewFilter(ThingFilter):
    search: Optional[str] = None


class ThingViewManager:
    @staticmethod
    def list(
        filters: ThingViewFilter = Query(),
    ) -> list[ThingView]:
        query = """
        SELECT t.id, t.category_id, c.name as category_name, t.name, t.description, t.docs_link 
        FROM things t
        LEFT JOIN categories c ON t.category_id = c.id
        WHERE t.name LIKE ?
        """
        params = [f"%{filters.name}%" if filters and filters.name else "%"]
        if filters:
            if filters.category_id is not None:
                query += " AND t.category_id = ?"
                params.append(str(filters.category_id))
            if filters.search:
                query += " AND (t.name LIKE ? OR t.description LIKE ?)"
                search_pattern = f"%{filters.search}%"
                params.extend([search_pattern, search_pattern])
        return Database.run_list(query, tuple(params), ThingView)
