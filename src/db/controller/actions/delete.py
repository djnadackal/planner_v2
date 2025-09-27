import logging

from ...core import DbCore, ExceptionPackage


logger = logging.getLogger(__name__)


def delete(action_id: int) -> None:
    logger.info(f"Deleting action with ID: {action_id}")
    query = "DELETE FROM actions WHERE id = ?"
    exception_package = ExceptionPackage(
        not_found_error=f"Action with ID {action_id} not found"
    )
    DbCore.run_delete(query, action_id, exception_package)
