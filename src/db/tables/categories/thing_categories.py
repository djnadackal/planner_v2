import logging

from .category_base import Category


logger = logging.getLogger(__name__)


# Pydantic model for Category
class ThingCategory(Category):
    __table_name__ = "thing_categories"
    __logger__ = logger
