from typing import Optional
from fastapi import APIRouter
from ..db import database


router = APIRouter(prefix="/thingView", tags=["thingView"])


views = database.views


@router.get("/", response_model=list[views.ThingView])
async def list_things(filters: Optional[views.ThingViewFilter] = None):
    """
    List things with optional filters (fuzzy search on name).
    """
    return views.ThingViewManager.list_thing_view(filters)
