import logging
from ...core import DbCore, ExceptionPackage


from .base import Ticket


logger = logging.getLogger(__name__)


core = DbCore()
core.logger = logger


def update(ticket: Ticket) -> None:
    if ticket.id is None:
        raise ValueError("Ticket ID is required for update")
    query, params = ticket.get_update_query()
    exception_package = ExceptionPackage(
        foreign_key_constraint_error=f"Invalid thing_id: {ticket.thing_id} or category_id: {ticket.category_id}",
        not_found_error=f"Ticket with ID {ticket.id} not found",
    )
    core.run_update(query, params, exception_package)
