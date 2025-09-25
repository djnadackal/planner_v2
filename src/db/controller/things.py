from pydantic import BaseModel
from typing import Optional, List

from ..core import Database, ExceptionPackage


# Pydantic model for Thing
class Thing(BaseModel):
    id: Optional[int] = None
    category_id: Optional[int] = None
    name: str
    description: Optional[str] = None
    docs_link: Optional[str] = None
    parent_id: Optional[int] = None

    class Config:
        from_attributes = True


# Pydantic model for Thing filter
class ThingFilter(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    parent_id: Optional[int] = None
    search: Optional[str] = None


# Manager class for CRUD operations
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
        return Database.run_create(query, params, exception_package)

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
        Database.run_update(query, params, exception_package)

    @staticmethod
    def get_by_id(thing_id: int) -> Optional[Thing]:
        query = "SELECT id, category_id, name, description, docs_link FROM things WHERE id = ?"
        return Database.run_get_by_id(query, thing_id, Thing)

    @staticmethod
    def list_things(filters: Optional[ThingFilter] = None) -> List[Thing]:
        query = "SELECT id, category_id, name, description, docs_link FROM things WHERE name LIKE ?"
        params = [f"%{filters.name if filters and filters.name else ''}%"]

        if filters and filters.category_id is not None:
            query += " AND category_id = ?"
            params.append(str(filters.category_id))
        if filters and filters.parent_id is not None:
            query += " AND parent_id = ?"
            params.append(str(filters.parent_id))
        if filters and filters.search is not None:
            query += " AND (name LIKE ? OR description LIKE ?)"
            search_param = f"%{filters.search}%"
            params.extend([search_param, search_param])
        return Database.run_list(query, tuple(params), Thing)

    @staticmethod
    def delete(thing_id: int) -> None:
        query = "DELETE FROM things WHERE id = ?"
        exception_package = ExceptionPackage(
            not_found_error=f"Thing with ID {thing_id} not found",
            foreign_key_constraint_error=f"Cannot delete thing ID {thing_id}: it is referenced by other records",
        )
        Database.run_delete(query, thing_id, exception_package)
