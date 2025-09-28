import logging
from typing import TYPE_CHECKING, Optional, List

from ..table_model import TableModel


logger = logging.getLogger(__name__)


if TYPE_CHECKING:
    from ..categories import ThingCategory


# Pydantic model for Thing
class Thing(TableModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    docs_link: Optional[str] = None

    category_id: Optional[int] = None
    parent_id: Optional[int] = None

    category: Optional["ThingCategory"] = None
    parent: Optional["Thing"] = None
    children: Optional[List["Thing"]] = None

    class Config:
        from_attributes = True
