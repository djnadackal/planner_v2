import logging

from .category_base import Category


logger = logging.getLogger(__name__)


# Pydantic model for Category
class TicketCategory(Category):
    __table_name__ = "ticket_categories"
    __logger__ = logger
