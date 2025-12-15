import logging

from ...core import DbCore, ExceptionPackage

from .base import Schedule


logger = logging.getLogger(__name__)

core = DbCore()
core.logger = logger


def update(schedule: Schedule) -> None:
    logger.info(f"Updating schedule: {schedule}")
    if schedule.id is None:
        raise ValueError("Schedule ID is required for update")
    query, params = schedule.get_update_query()
    exception_package = ExceptionPackage(
        not_found_error=f"Schedule with ID {schedule.id} not found"
    )
    core.run_update(query, params, exception_package)
