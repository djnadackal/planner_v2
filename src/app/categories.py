from typing import Optional
from fastapi import APIRouter, HTTPException, status
from ..db import controller as db


router = APIRouter(prefix="/categories", tags=["categories"])


# Categories Routes
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(category: db.Category):
    """
    Create a new category.
    Returns the ID of the created category.
    """
    try:
        category_id = db.CategoryManager.create(category)
        return {"id": category_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{category_id}")
async def update_category(category_id: int, category: db.Category):
    """
    Update a category by ID.
    """
    category.id = category_id
    try:
        db.CategoryManager.update(category)
        return {"message": "Category updated"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{category_id}", response_model=db.Category)
async def get_category(category_id: int):
    """
    Get a category by ID.
    """
    category = db.CategoryManager.get_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("/", response_model=list[db.Category])
async def list_categories(filters: Optional[db.CategoryFilter] = None):
    """
    List categories with optional filters (fuzzy search on name).
    """
    return db.CategoryManager.list_categories(filters)


@router.delete("/{category_id}")
async def delete_category(category_id: int):
    """
    Delete a category by ID.
    """
    try:
        db.CategoryManager.delete(category_id)
        return {"message": "Category deleted"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
