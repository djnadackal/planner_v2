from pydantic import BaseModel
from typing import TYPE_CHECKING, Optional, List
from datetime import datetime

from ..core import DbCore, ExceptionPackage


if TYPE_CHECKING:
    from .tickets import Ticket


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
        query = (
            "INSERT INTO actions (ticket_id, action_type) VALUES (?, ?)"
        )
        params = (action.ticket_id, action.action_type)
        exception_package = ExceptionPackage(
            foreign_key_constraint_error=f"Invalid ticket_id: {action.ticket_id}"
        )
        last_row_id = DbCore.run_create(query, params, exception_package)
        return last_row_id

    @staticmethod
    def update(action: Action) -> None:
        if action.id is None:
            raise ValueError("Action ID is required for update")
        query = "UPDATE actions SET ticket_id = ?, action_type = ? WHERE id = ?"
        params = (action.ticket_id, action.action_type, action.id)
        exception_package = ExceptionPackage(
            foreign_key_constraint_error=f"Invalid ticket_id: {action.ticket_id}",
            not_found_error=f"Action with ID {action.id} not found",
        )
        DbCore.run_update(query, params, exception_package)

    @staticmethod
    def get_by_id(action_id: int) -> Optional[Action]:
        query = "SELECT id, ticket_id, action_type, performed_at FROM actions WHERE id = ?"
        return DbCore.run_get_by_id(query, action_id, Action)

    @staticmethod
    def list_actions(
        filters: Optional[ActionFilter] = None,
    ) -> List[Action]:
        query = "SELECT id, ticket_id, action_type, performed_at FROM actions WHERE action_type LIKE ?"
        params = [
            f"%{filters.action_type if filters and filters.action_type else ''}%"
        ]

        if filters:
            if filters.ticket_id is not None:
                query += " AND ticket_id = ?"
                params.append(str(filters.ticket_id))

        return DbCore.run_list(query, tuple(params), Action)

    @staticmethod
    def delete(action_id: int) -> None:
        query = "DELETE FROM actions WHERE id = ?"
        exception_package = ExceptionPackage(
            not_found_error=f"Action with ID {action_id} not found"
        )
        DbCore.run_delete(query, action_id, exception_package)
