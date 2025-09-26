import logging
from pydantic import BaseModel, Field
from typing import Literal, Optional, List

from .thing_categories import ThingCategory

from ..core import DbCore, ExceptionPackage


logger = logging.getLogger(__name__)


# Pydantic model for Thing
class Thing(BaseModel):
    id: Optional[int] = None
    category_id: Optional[int] = None
    name: str
    description: Optional[str] = None
    docs_link: Optional[str] = None
    parent_id: Optional[int] = None
    category: Optional["ThingCategory"] = None
    parent: Optional["Thing"] = None
    children: Optional[List["Thing"]] = None

    class Config:
        from_attributes = True

    @classmethod
    def from_row(cls, row) -> "Thing":
        thing = cls(
            id=row["id"],
            category_id=row["category_id"],
            name=row["name"],
            description=row["description"],
            docs_link=row["docs_link"],
            parent_id=row["parent_id"],
        )
        if "category_name" in row.keys():
            thing.category = ThingCategory(
                id=row["category_id"],
                name=row.get("category_name", None),
                description=row.get("category_description", None),
            )
        if "parent_name" in row.keys():
            thing.parent = Thing(
                id=row["parent_id"],
                name=row.get("parent_name", None),
                description=row.get("parent_description", None),
                docs_link=row.get("parent_docs_link", None),
            )
        return thing

    def populate_children(self) -> None:
        if self.id is None:
            self.children = []
            return
        query = "SELECT id, category_id, name, description, docs_link, parent_id FROM things WHERE parent_id = ?"
        self.children = DbCore.run_list(query, (self.id,), Thing)


# Pydantic model for Thing filter
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


class ThingManager:
    @staticmethod
    def create(thing: Thing) -> int:
        query = "INSERT INTO things (category_id, name, description, docs_link) VALUES (?, ?, ?, ?)"
        params = (
            thing.category_id,
            thing.name,
            thing.description,
            thing.docs_link,
        )
        exception_package = ExceptionPackage(
            unique_constraint_error=f"Thing name '{thing.name}' already exists",
            foreign_key_constraint_error=f"Invalid category_id: {thing.category_id}",
        )
        return DbCore.run_create(query, params, exception_package)

    @staticmethod
    def update(thing: Thing) -> None:
        if thing.id is None:
            raise ValueError("Thing ID is required for update")
        query = "UPDATE things SET category_id = ?, name = ?, description = ?, docs_link = ? WHERE id = ?"
        params = (
            thing.category_id,
            thing.name,
            thing.description,
            thing.docs_link,
            thing.id,
        )
        exception_package = ExceptionPackage(
            unique_constraint_error=f"Thing name '{thing.name}' already exists",
            foreign_key_constraint_error=f"Invalid category_id: {thing.category_id}",
            not_found_error=f"Thing with ID {thing.id} not found",
        )
        DbCore.run_update(query, params, exception_package)

    @staticmethod
    def get_by_id(thing_id: int) -> Optional[Thing]:
        query = "SELECT id, category_id, name, description, docs_link FROM things WHERE id = ?"
        return DbCore.run_get_by_id(query, thing_id, Thing)

    @staticmethod
    def list_things(
        query_params: Optional[ThingParams] = None,
    ) -> List[Thing]:
        select = "SELECT t.id, t.category_id, t.name, t.description, t.docs_link"
        from_clause = "FROM things t"
        where_seed = "WHERE 1=1"
        params = []
        if query_params and query_params.include:
            join_clauses = []
            if "category" in query_params.include:
                select += ", c.name AS category_name, c.description AS category_description"
                join_clauses.append(
                    "LEFT JOIN thing_categories c ON t.category_id = c.id"
                )
            if "parent" in query_params.include:
                select += ", p.name AS parent_name, p.description AS parent_description, p.docs_link AS parent_docs_link"
                join_clauses.append(
                    "LEFT JOIN things p ON t.parent_id = p.id"
                )
            query = f"{select} {from_clause} {' '.join(join_clauses)} {where_seed}"
        else:
            query = f"{select} {from_clause} {where_seed}"

        if query_params:
            if query_params.name is not None:
                query += " AND t.name LIKE ?"
                params.append(f"%{query_params.name}%")
            if query_params.category_id is not None:
                query += " AND t.category_id = ?"
                params.append(str(query_params.category_id))
            if query_params.parent_id == 0:
                query += " AND t.parent_id IS NULL"
            elif query_params.parent_id is not None:
                query += " AND t.parent_id = ?"
                params.append(str(query_params.parent_id))
            if query_params.search is not None:
                query += " AND (t.name LIKE ? OR t.description LIKE ?)"
                search_param = f"%{query_params.search}%"
                params.extend([search_param, search_param])
        things = DbCore.run_list(query, tuple(params), Thing.from_row)
        if query_params and "children" in query_params.include:
            for thing in things:
                thing.populate_children()
        return things

    @staticmethod
    def delete(thing_id: int) -> None:
        query = "DELETE FROM things WHERE id = ?"
        exception_package = ExceptionPackage(
            not_found_error=f"Thing with ID {thing_id} not found",
            foreign_key_constraint_error=f"Cannot delete thing ID {thing_id}: it is referenced by other records",
        )
        DbCore.run_delete(query, thing_id, exception_package)
