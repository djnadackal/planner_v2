import logging
from typing import Optional

from ....core import ColumnField, PrimaryKeyField, TableModel


class Category(TableModel):
    # config
    __category_model__ = "Category"
    __logger__ = logging.getLogger(__name__)
    # fields
    id: Optional[int] = PrimaryKeyField(None)
    name: Optional[str] = ColumnField(None)
    description: Optional[str] = ColumnField(None)
    is_default: bool = ColumnField(False)
    color: Optional[str] = ColumnField(None)

    class Config:
        from_attributes = True
