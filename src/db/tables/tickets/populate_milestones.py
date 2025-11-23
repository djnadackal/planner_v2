import logging

from ...core import DbCore

from .base import Ticket


logger = logging.getLogger(__name__)


core = DbCore()
core.logger = logger


def populate_milestones(ticket: Ticket) -> None:
    from ..milestones import Milestone

    if ticket.id is None:
        ticket.children = []
        return
    query = (
        "Select m.* FROM milestones m "
        "JOIN ticket_milestones tm ON m.id = tm.milestone_id "
        "WHERE tm.ticket_id = ?"
    )
    ticket.children = core.run_list(
        query, (ticket.id,), Milestone.from_row
    )
