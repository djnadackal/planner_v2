import sqlite3
from pydantic import BaseModel
from typing import Optional, List
from ..util import get_db_connection


# Pydantic model for Thing
class Thing(BaseModel):
    id: Optional[int] = None
    category_id: Optional[int] = None
    name: str
    description: Optional[str] = None
    docs_link: Optional[str] = None

    class Config:
        from_attributes = True


# Pydantic model for Thing filter
class ThingFilter(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None


# Manager class for CRUD operations
class ThingManager:
    @staticmethod
    def create(thing: Thing) -> int:
        """
        Create a new thing.
        Pseudocode:
        1. Connect to database via util
        2. Insert thing (category_id, name, description, docs_link)
        3. Return new thing ID
        4. Handle unique name and foreign key constraints
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO things (category_id, name, description, docs_link) VALUES (?, ?, ?, ?)",
                    (
                        thing.category_id,
                        thing.name,
                        thing.description,
                        thing.docs_link,
                    ),
                )
                if not cursor.lastrowid:
                    raise ValueError("Failed to create thing")
                return cursor.lastrowid
            except sqlite3.IntegrityError as e:
                if "UNIQUE constraint failed" in str(e):
                    raise ValueError(
                        f"Thing name '{thing.name}' already exists"
                    )
                if "FOREIGN KEY constraint failed" in str(e):
                    raise ValueError(
                        f"Invalid category_id: {thing.category_id}"
                    )
                raise e

    @staticmethod
    def update(thing: Thing) -> None:
        """
        Update an existing thing.
        Pseudocode:
        1. Connect to database via util
        2. Update category_id, name, description, docs_link where id matches
        3. Handle missing ID or constraints
        """
        if thing.id is None:
            raise ValueError("Thing ID is required for update")
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "UPDATE things SET category_id = ?, name = ?, description = ?, docs_link = ? WHERE id = ?",
                    (
                        thing.category_id,
                        thing.name,
                        thing.description,
                        thing.docs_link,
                        thing.id,
                    ),
                )
                if cursor.rowcount == 0:
                    raise ValueError(f"Thing with ID {thing.id} not found")
            except sqlite3.IntegrityError as e:
                if "UNIQUE constraint failed" in str(e):
                    raise ValueError(
                        f"Thing name '{thing.name}' already exists"
                    )
                if "FOREIGN KEY constraint failed" in str(e):
                    raise ValueError(
                        f"Invalid category_id: {thing.category_id}"
                    )
                raise e

    @staticmethod
    def get_by_id(thing_id: int) -> Optional[Thing]:
        """
        Get a thing by ID.
        Pseudocode:
        1. Connect to database via util
        2. Select thing by ID
        3. Return Thing model or None if not found
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, category_id, name, description, docs_link FROM things WHERE id = ?",
                (thing_id,),
            )
            row = cursor.fetchone()
            return Thing(**row) if row else None

    @staticmethod
    def list_things(filters: Optional[ThingFilter] = None) -> List[Thing]:
        """
        List things with mandatory fuzzy search on name and optional category_id filter.
        Pseudocode:
        1. Connect to database via util
        2. Build query with mandatory name LIKE clause
        3. Add category_id filter if provided
        4. Execute query and return list of Thing models
        """
        query = "SELECT id, category_id, name, description, docs_link FROM things WHERE name LIKE ?"
        params = [f"%{filters.name if filters and filters.name else ''}%"]

        if filters and filters.category_id is not None:
            query += " AND category_id = ?"
            params.append(str(filters.category_id))

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [Thing(**row) for row in rows]

    @staticmethod
    def delete(thing_id: int) -> None:
        """
        Delete a thing by ID.
        Pseudocode:
        1. Connect to database via util
        2. Delete thing by ID
        3. Handle missing ID or foreign key constraints
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "DELETE FROM things WHERE id = ?", (thing_id,)
                )
                if cursor.rowcount == 0:
                    raise ValueError(f"Thing with ID {thing_id} not found")
            except sqlite3.IntegrityError:
                raise ValueError(
                    f"Cannot delete thing ID {thing_id}: it is referenced by other records"
                )
