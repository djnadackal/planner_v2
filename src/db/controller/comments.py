import sqlite3
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from ..util import get_db_connection


# Pydantic model for Comment
class Comment(BaseModel):
    id: Optional[int] = None
    ticket_id: Optional[int] = None
    content: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Pydantic model for Comment filter
class CommentFilter(BaseModel):
    content: Optional[str] = None
    ticket_id: Optional[int] = None


# Manager class for CRUD operations
class CommentManager:
    @staticmethod
    def create(comment: Comment) -> int:
        """
        Create a new comment.
        Pseudocode:
        1. Connect to database via util
        2. Insert comment (ticket_id, content)
        3. Return new comment ID
        4. Handle foreign key constraints
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO comments (ticket_id, content) VALUES (?, ?)",
                    (comment.ticket_id, comment.content),
                )
                if not cursor.lastrowid:
                    raise ValueError("Failed to create comment")
                return cursor.lastrowid
            except sqlite3.IntegrityError as e:
                if "FOREIGN KEY constraint failed" in str(e):
                    raise ValueError(
                        f"Invalid ticket_id: {comment.ticket_id}"
                    )
                raise e

    @staticmethod
    def update(comment: Comment) -> None:
        """
        Update an existing comment.
        Pseudocode:
        1. Connect to database via util
        2. Update content where id matches
        3. Handle missing ID
        """
        if comment.id is None:
            raise ValueError("Comment ID is required for update")
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "UPDATE comments SET content = ? WHERE id = ?",
                    (comment.content, comment.id),
                )
                if cursor.rowcount == 0:
                    raise ValueError(
                        f"Comment with ID {comment.id} not found"
                    )
            except sqlite3.IntegrityError as e:
                raise e

    @staticmethod
    def get_by_id(comment_id: int) -> Optional[Comment]:
        """
        Get a comment by ID.
        Pseudocode:
        1. Connect to database via util
        2. Select comment by ID
        3. Return Comment model or None if not found
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, ticket_id, content, created_at FROM comments WHERE id = ?",
                (comment_id,),
            )
            row = cursor.fetchone()
            return Comment(**row) if row else None

    @staticmethod
    def list_comments(
        filters: Optional[CommentFilter] = None,
    ) -> List[Comment]:
        """
        List comments with mandatory fuzzy search on content and optional ticket_id filter.
        Pseudocode:
        1. Connect to database via util
        2. Build query with mandatory content LIKE clause
        3. Add ticket_id filter if provided
        4. Execute query and return list of Comment models
        """
        query = "SELECT id, ticket_id, content, created_at FROM comments WHERE content LIKE ?"
        params = [
            f"%{filters.content if filters and filters.content else ''}%"
        ]

        if filters and filters.ticket_id is not None:
            query += " AND ticket_id = ?"
            params.append(str(filters.ticket_id))

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [Comment(**row) for row in rows]

    @staticmethod
    def delete(comment_id: int) -> None:
        """
        Delete a comment by ID.
        Pseudocode:
        1. Connect to database via util
        2. Delete comment by ID
        3. Handle missing ID
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM comments WHERE id = ?", (comment_id,)
            )
            if cursor.rowcount == 0:
                raise ValueError(f"Comment with ID {comment_id} not found")
