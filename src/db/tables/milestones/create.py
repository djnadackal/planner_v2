import logging

from ...core import DbCore, ExceptionPackage, InsertBuilder

from .base import Milestone

logger = logging.getLogger(__name__)

core = DbCore()
core.logger = logger


def create(milestone: Milestone) -> int:
    logger.info(f"Creating new milestone: {milestone}")
    query, params = InsertBuilder(milestone).query
    logger.info(f"Milestone Create Query: {query} \n Params: {params}")
    exception_package = ExceptionPackage()
    last_row_id = core.run_create(query, params, exception_package)
    milestone.id = last_row_id
    return last_row_id
