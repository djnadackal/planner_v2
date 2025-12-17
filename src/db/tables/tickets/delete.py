import logging

from ...core import DbCore, ExceptionPackage

from .base import Ticket

logger = logging.getLogger(__name__)

core = DbCore()
core.logger = logger


def delete(ticket_id: int) -> None:
    query = Ticket.get_delete_query()
    exception_package = ExceptionPackage(
        not_found_error=f"Ticket with ID {ticket_id} not found"
    )
    return core.run_delete(query, ticket_id, exception_package)
