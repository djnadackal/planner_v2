import logging

from ...core import DbCore


from .base import Ticket


logger = logging.getLogger(__name__)


core = DbCore()
core.logger = logger


def add_milestone(ticket: Ticket, milestone_id: int) -> None:
    logger.info(
        f"Adding ticket ID {ticket.id} to milestone ID {milestone_id}"
    )
    if ticket.id is None:
        raise ValueError("Ticket ID is required to add a milestone")
    query = "INSERT INTO ticket_milestones (ticket_id, milestone_id) VALUES (?, ?)"
    params = (ticket.id, milestone_id)
    core.execute_sql(query, params)
