import logging

from ...core import DbCore


from .base import Ticket


logger = logging.getLogger(__name__)


core = DbCore()
core.logger = logger


def remove_milestone(ticket: Ticket, milestone_id: int) -> None:
    logger.info(
        f"Removing ticket ID {ticket.id} to milestone ID {milestone_id}"
    )
    if ticket.id is None:
        raise ValueError("Ticket ID is required to add a milestone")
    query = "DELETE FROM ticket_milestones WHERE ticket_id = ? AND milestone_id = ?"
    params = (ticket.id, milestone_id)
    core.execute_sql(query, params)
