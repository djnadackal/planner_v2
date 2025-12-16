import logging

from ...core import DbCore, ExceptionPackage

from .base import Schedule

logger = logging.getLogger(__name__)

core = DbCore()
core.logger = logger


def delete(schedule_id: int) -> None:
    logger.info(f"Deleting Schedule with ID: {schedule_id}")
    query = Schedule.get_delete_query()
    exception_package = ExceptionPackage(
        not_found_error=f"Milestone with ID {schedule_id} not found"
    )
    core.run_delete(query, schedule_id, exception_package)
