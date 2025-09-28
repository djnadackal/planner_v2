import logging
from .category_base import Category


logger = logging.getLogger(__name__)


class ActionType(Category):
    __table_name__ = "action_types"
    __logger__ = logger
