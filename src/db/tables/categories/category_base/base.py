import logging
from typing import Optional

from pydantic import BaseModel

from ...table_model import TableModel


class Category(TableModel):
    # config
    __table_name__ = "categories"
    __category_model__ = "Category"
    __logger__ = logging.getLogger(__name__)
    # fields
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True
