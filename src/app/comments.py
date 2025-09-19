from typing import Optional
from fastapi import APIRouter, HTTPException, status
from ..db import controller as db


router = APIRouter(prefix="/comments", tags=["comments"])


# Comments Routes
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_comment(comment: db.Comment):
    """
    Create a new comment.
    Returns the ID of the created comment.
    """
    try:
        comment_id = db.CommentManager.create(comment)
        return {"id": comment_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{comment_id}")
async def update_comment(comment_id: int, comment: db.Comment):
    """
    Update a comment by ID.
    """
    comment.id = comment_id
    try:
        db.CommentManager.update(comment)
        return {"message": "Comment updated"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{comment_id}", response_model=db.Comment)
async def get_comment(comment_id: int):
    """
    Get a comment by ID.
    """
    comment = db.CommentManager.get_by_id(comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@router.get("/", response_model=list[db.Comment])
async def list_comments(filters: Optional[db.CommentFilter] = None):
    """
    List comments with optional filters (fuzzy search on content).
    """
    return db.CommentManager.list_comments(filters)


@router.delete("/{comment_id}")
async def delete_comment(comment_id: int):
    """
    Delete a comment by ID.
    """
    try:
        db.CommentManager.delete(comment_id)
        return {"message": "Comment deleted"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
