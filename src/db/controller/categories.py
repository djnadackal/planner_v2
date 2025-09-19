import sqlite3
from pydantic import BaseModel
from typing import Optional, List
from ..util import get_db_connection


# Pydantic model for Category
class Category(BaseModel):
    id: Optional[int] = None
    name: str
    parent_id: Optional[int] = None

    class Config:
        from_attributes = True


# Pydantic model for Category filter
class CategoryFilter(BaseModel):
    name: Optional[str] = None
    parent_id: Optional[int] = None


# Manager class for CRUD operations
class CategoryManager:
    @staticmethod
    def create(category: Category) -> int:
        """
        Create a new category.
        Pseudocode:
        1. Connect to database
        2. Insert category (name, parent_id)
        3. Return new category ID
        4. Handle unique name constraint
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO categories (name, parent_id) VALUES (?, ?)",
                    (category.name, category.parent_id),
                )
                if not cursor.lastrowid:
                    raise ValueError("Failed to create category")
                return cursor.lastrowid
            except sqlite3.IntegrityError as e:
                if "UNIQUE constraint failed" in str(e):
                    raise ValueError(
                        f"Category name '{category.name}' already exists"
                    )
                if "FOREIGN KEY constraint failed" in str(e):
                    raise ValueError(
                        f"Invalid parent_id: {category.parent_id}"
                    )
                raise e

    @staticmethod
    def update(category: Category) -> None:
        """
        Update an existing category.
        Pseudocode:
        1. Connect to database
        2. Update name and parent_id where id matches
        3. Handle missing ID or unique name constraint
        """
        if category.id is None:
            raise ValueError("Category ID is required for update")
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "UPDATE categories SET name = ?, parent_id = ? WHERE id = ?",
                    (category.name, category.parent_id, category.id),
                )
                if cursor.rowcount == 0:
                    raise ValueError(
                        f"Category with ID {category.id} not found"
                    )
            except sqlite3.IntegrityError as e:
                if "UNIQUE constraint failed" in str(e):
                    raise ValueError(
                        f"Category name '{category.name}' already exists"
                    )
                if "FOREIGN KEY constraint failed" in str(e):
                    raise ValueError(
                        f"Invalid parent_id: {category.parent_id}"
                    )
                raise e

    @staticmethod
    def get_by_id(category_id: int) -> Optional[Category]:
        """
        Get a category by ID.
        Pseudocode:
        1. Connect to database
        2. Select category by ID
        3. Return Category model or None if not found
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, parent_id FROM categories WHERE id = ?",
                (category_id,),
            )
            row = cursor.fetchone()
            return Category(**row) if row else None

    @staticmethod
    def list_categories(
        filters: Optional[CategoryFilter] = None,
    ) -> List[Category]:
        """
        List categories with mandatory fuzzy search on name and optional parent_id filter.
        Pseudocode:
        1. Connect to database
        2. Build query with mandatory name LIKE clause
        3. Add parent_id filter if provided
        4. Execute query and return list of Category models
        """
        query = (
            "SELECT id, name, parent_id FROM categories WHERE name LIKE ?"
        )
        params = [f"%{filters.name if filters and filters.name else ''}%"]

        if filters and filters.parent_id is not None:
            query += " AND parent_id = ?"
            params.append(str(filters.parent_id))

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [Category(**row) for row in rows]

    @staticmethod
    def delete(category_id: int) -> None:
        """
        Delete a category by ID.
        Pseudocode:
        1. Connect to database
        2. Delete category by ID
        3. Handle missing ID or foreign key constraints
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "DELETE FROM categories WHERE id = ?", (category_id,)
                )
                if cursor.rowcount == 0:
                    raise ValueError(
                        f"Category with ID {category_id} not found"
                    )
            except sqlite3.IntegrityError:
                raise ValueError(
                    f"Cannot delete category ID {category_id}: it is referenced by other records"
                )
