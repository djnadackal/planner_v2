import logging

from ...core import DbCore, ExceptionPackage

from .base import Milestone


logger = logging.getLogger(__name__)

core = DbCore()
core.logger = logger


def update(milestone: Milestone) -> None:
    logger.info(f"Updating Milestone: {milestone}")
    if milestone.id is None:
        raise ValueError("Milestone ID is required for update")
    query, params = milestone.get_update_query()
    exception_package = ExceptionPackage(
        not_found_error=f"Milestone with ID {milestone.id} not found"
    )
    core.run_update(query, params, exception_package)
