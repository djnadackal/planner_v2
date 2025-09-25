from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from ..core import DbCore, ExceptionPackage


# Pydantic model for Ticket
class Ticket(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    thing_id: Optional[int] = None
    category_id: Optional[int] = None
    description: str
    created_at: Optional[datetime] = None
    open: Optional[bool] = True
    updated_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Pydantic model for Ticket filter
class TicketFilter(BaseModel):
    thing_id: Optional[int] = None
    category_id: Optional[int] = None
    open: Optional[bool] = None
    search: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    completed_after: Optional[datetime] = None
    completed_before: Optional[datetime] = None


# Manager class for CRUD operations
class TicketManager:
    @staticmethod
    def create(ticket: Ticket) -> int:
        query = "INSERT INTO tickets (thing_id, category_id, description, open) VALUES (?, ?, ?, ?)"
        params = (
            ticket.thing_id,
            ticket.category_id,
            ticket.description,
            ticket.open,
        )
        exception_package = ExceptionPackage(
            foreign_key_constraint_error=f"Invalid thing_id: {ticket.thing_id} or category_id: {ticket.category_id}"
        )
        last_row_id = DbCore.run_create(query, params, exception_package)
        return last_row_id

    @staticmethod
    def update(ticket: Ticket) -> None:
        if ticket.id is None:
            raise ValueError("Ticket ID is required for update")
        query = "UPDATE tickets SET thing_id = ?, category_id = ?, description = ?, open = ?, updated_at = CURRENT_TIMESTAMP, completed_at = ? WHERE id = ?"
        params = (
            ticket.thing_id,
            ticket.category_id,
            ticket.description,
            ticket.open,
            ticket.completed_at,
            ticket.id,
        )
        exception_package = ExceptionPackage(
            foreign_key_constraint_error=f"Invalid thing_id: {ticket.thing_id} or category_id: {ticket.category_id}",
            not_found_error=f"Ticket with ID {ticket.id} not found",
        )
        DbCore.run_update(query, params, exception_package)

    @staticmethod
    def get_by_id(ticket_id: int) -> Optional[Ticket]:
        query = "SELECT id, thing_id, category_id, description, created_at, open, updated_at, completed_at FROM tickets WHERE id = ?"
        return DbCore.run_get_by_id(query, ticket_id, Ticket)

    @staticmethod
    def list_tickets(
        filters: Optional[TicketFilter] = None,
    ) -> List[Ticket]:
        query = "SELECT id, thing_id, category_id, description, created_at, open, updated_at, completed_at FROM tickets WHERE 1=1"
        params = []

        if filters:
            if filters.thing_id is not None:
                query += " AND thing_id = ?"
                params.append(str(filters.thing_id))
            if filters.category_id is not None:
                query += " AND category_id = ?"
                params.append(str(filters.category_id))
            if filters.open is not None:
                query += " AND open = ?"
                params.append(str(filters.open).upper())
            if filters.search is not None:
                query += " AND (description LIKE ? OR title LIKE ?)"
                search_param = f"%{filters.search}%"
                params.extend([search_param, search_param])
            if filters.created_after is not None:
                query += " AND created_at >= ?"
                params.append(filters.created_after.isoformat())
            if filters.created_before is not None:
                query += " AND created_at <= ?"
                params.append(filters.created_before.isoformat())
            if filters.updated_after is not None:
                query += " AND updated_at >= ?"
                params.append(filters.updated_after.isoformat())
            if filters.updated_before is not None:
                query += " AND updated_at <= ?"
                params.append(filters.updated_before.isoformat())
            if filters.completed_after is not None:
                query += " AND completed_at >= ?"
                params.append(filters.completed_after.isoformat())
            if filters.completed_before is not None:
                query += " AND completed_at <= ?"
                params.append(filters.completed_before.isoformat())
        return DbCore.run_list(query, tuple(params), Ticket)

    @staticmethod
    def delete(ticket_id: int) -> None:
        query = "DELETE FROM tickets WHERE id = ?"
        exception_package = ExceptionPackage(
            not_found_error=f"Ticket with ID {ticket_id} not found"
        )
        return DbCore.run_delete(query, ticket_id, exception_package)
