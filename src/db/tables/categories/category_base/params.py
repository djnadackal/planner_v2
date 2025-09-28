from typing import Optional

from pydantic import BaseModel


class CategoryParams(BaseModel):
    name: Optional[str] = None
    search: Optional[str] = None
