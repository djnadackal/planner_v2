from fastapi import APIRouter, HTTPException, Query, status
from ..db import Controller


router = APIRouter(prefix="/actions", tags=["actions"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_action(action: Controller.Tables.Action):
    """
    Create a new action.
    Returns the ID of the created action.
    """
    try:
        action_id = Controller.Tables.Action.create(action)
        return {"id": action_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{action_id}")
async def update_action(action_id: int, action: Controller.Tables.Action):
    """
    Update an action by ID.
    """
    action.id = action_id
    try:
        Controller.Tables.Action.update(action)
        return {"message": "Action updated"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{action_id}", response_model=Controller.Tables.Action)
async def get_action(action_id: int):
    """
    Get an action by ID.
    """
    action = Controller.Tables.Action.get_by_id(action_id)
    if not action:
        raise HTTPException(status_code=404, detail="Action not found")
    return action


@router.get("/", response_model=list[Controller.Tables.Action])
async def list_actions(filters: Controller.Params.Action = Query()):
    """
    List actions with optional filters (fuzzy search on action_type).
    """
    return Controller.Tables.Action.read(filters)


@router.delete("/{action_id}")
async def delete_action(action_id: int):
    """
    Delete an action by ID.
    """
    try:
        Controller.Tables.Action.delete(action_id)
        return {"message": "Action deleted"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
