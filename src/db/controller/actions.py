import sqlite3
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from ..util import get_db_connection


# Pydantic model for Action
class Action(BaseModel):
    id: Optional[int] = None
    ticket_id: Optional[int] = None
    action_type: str
    performed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Pydantic model for Action filter
class ActionFilter(BaseModel):
    action_type: Optional[str] = None
    ticket_id: Optional[int] = None


# Manager class for CRUD operations
class ActionManager:
    @staticmethod
    def create(action: Action) -> int:
        """
        Create a new action.
        Pseudocode:
        1. Connect to database via util
        2. Insert action (ticket_id, action_type)
        3. Return new action ID
        4. Handle foreign key constraints
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO actions (ticket_id, action_type) VALUES (?, ?)",
                    (action.ticket_id, action.action_type),
                )
                if not cursor.lastrowid:
                    raise ValueError("Failed to create action")
                return cursor.lastrowid
            except sqlite3.IntegrityError as e:
                if "FOREIGN KEY constraint failed" in str(e):
                    raise ValueError(
                        f"Invalid ticket_id: {action.ticket_id}"
                    )
                raise e

    @staticmethod
    def update(action: Action) -> None:
        """
        Update an existing action.
        Pseudocode:
        1. Connect to database via util
        2. Update ticket_id and action_type where id matches
        3. Handle missing ID or constraints
        """
        if action.id is None:
            raise ValueError("Action ID is required for update")
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "UPDATE actions SET ticket_id = ?, action_type = ? WHERE id = ?",
                    (action.ticket_id, action.action_type, action.id),
                )
                if cursor.rowcount == 0:
                    raise ValueError(
                        f"Action with ID {action.id} not found"
                    )
            except sqlite3.IntegrityError as e:
                if "FOREIGN KEY constraint failed" in str(e):
                    raise ValueError(
                        f"Invalid ticket_id: {action.ticket_id}"
                    )
                raise e

    @staticmethod
    def get_by_id(action_id: int) -> Optional[Action]:
        """
        Get an action by ID.
        Pseudocode:
        1. Connect to database via util
        2. Select action by ID
        3. Return Action model or None if not found
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, ticket_id, action_type, performed_at FROM actions WHERE id = ?",
                (action_id,),
            )
            row = cursor.fetchone()
            return Action(**row) if row else None

    @staticmethod
    def list_actions(
        filters: Optional[ActionFilter] = None,
    ) -> List[Action]:
        """
        List actions with mandatory fuzzy search on action_type and optional ticket_id filter.
        Pseudocode:
        1. Connect to database via util
        2. Build query with mandatory action_type LIKE clause
        3. Add ticket_id filter if provided
        4. Execute query and return list of Action models
        """
        query = "SELECT id, ticket_id, action_type, performed_at FROM actions WHERE action_type LIKE ?"
        params = [
            f"%{filters.action_type if filters and filters.action_type else ''}%"
        ]

        if filters and filters.ticket_id is not None:
            query += " AND ticket_id = ?"
            params.append(str(filters.ticket_id))

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [Action(**row) for row in rows]

    @staticmethod
    def delete(action_id: int) -> None:
        """
        Delete an action by ID.
        Pseudocode:
        1. Connect to database via util
        2. Delete action by ID
        3. Handle missing ID
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM actions WHERE id = ?", (action_id,)
            )
            if cursor.rowcount == 0:
                raise ValueError(f"Action with ID {action_id} not found")
