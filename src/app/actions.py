from typing import Optional
from fastapi import APIRouter, HTTPException, status
from ..db import controller as db


router = APIRouter(prefix="/actions", tags=["actions"])


# Actions Routes
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_action(action: db.Action):
    """
    Create a new action.
    Returns the ID of the created action.
    """
    try:
        action_id = db.ActionManager.create(action)
        return {"id": action_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{action_id}")
async def update_action(action_id: int, action: db.Action):
    """
    Update an action by ID.
    """
    action.id = action_id
    try:
        db.ActionManager.update(action)
        return {"message": "Action updated"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{action_id}", response_model=db.Action)
async def get_action(action_id: int):
    """
    Get an action by ID.
    """
    action = db.ActionManager.get_by_id(action_id)
    if not action:
        raise HTTPException(status_code=404, detail="Action not found")
    return action


@router.get("/", response_model=list[db.Action])
async def list_actions(filters: Optional[db.ActionFilter] = None):
    """
    List actions with optional filters (fuzzy search on action_type).
    """
    return db.ActionManager.list_actions(filters)


@router.delete("/{action_id}")
async def delete_action(action_id: int):
    """
    Delete an action by ID.
    """
    try:
        db.ActionManager.delete(action_id)
        return {"message": "Action deleted"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
