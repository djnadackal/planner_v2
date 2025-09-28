import logging
from typing import Optional

from ...core import DbCore

from .base import Comment


logger = logging.getLogger(__name__)


def get_by_id(comment_id: int) -> Optional[Comment]:
    logger.info(f"Getting Comment by ID: {comment_id}")
    query = "SELECT id, ticket_id, content, created_at FROM comments WHERE id = ?"
    return DbCore.run_get_by_id(query, comment_id, Comment)
