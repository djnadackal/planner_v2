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
    # add the join record
    query = "INSERT INTO ticket_milestones (ticket_id, milestone_id) VALUES (?, ?)"
    params = (ticket.id, milestone_id)
    core.execute_sql(query, params)
    # if the milestone has a due date, and the ticket has no due date or a later due date, update the ticket's due date
    from ..milestones.base import Milestone

    milestone: Milestone = Milestone.get_by_id(milestone_id)  # type: ignore
    if milestone.due_date is not None:
        if ticket.due_date is None or milestone.due_date < ticket.due_date:
            logger.info(
                f"Updating ticket ID {ticket.id} due date to milestone due date {milestone.due_date}"
            )
            ticket.due_date = milestone.due_date
            ticket.update()
