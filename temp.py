# app.py (or wherever you create FastAPI app)
from fastapi import FastAPI
from pydantic import BaseModel
import inspect
from src.db.tables import (
    ThingCategory,
    TicketCategory,
    ActionType,
    Action,
    Comment,
    Thing,
    Ticket,
    Milestone,
    User,
    CategoryParams,
    ReadCategoriesResponse,
    ActionParams,
    ReadActionsResponse,
    CommentParams,
    ReadCommentsResponse,
    ThingParams,
    ReadThingsResponse,
    TicketParams,
    ReadTicketsResponse,
    MilestoneParams,
    ReadMilestonesResponse,
    UserParams,
    ReadUsersResponse,
)

app = FastAPI()

# List your models here
models = [
    ThingCategory,
    TicketCategory,
    ActionType,
    Action,
    Comment,
    Thing,
    Ticket,
    Milestone,
    User,
    CategoryParams,
    ReadCategoriesResponse,
    ActionParams,
    ReadActionsResponse,
    CommentParams,
    ReadCommentsResponse,
    ThingParams,
    ReadThingsResponse,
    TicketParams,
    ReadTicketsResponse,
    MilestoneParams,
    ReadMilestonesResponse,
    UserParams,
    ReadUsersResponse,
]  # replace with actual

for model in models:
    try:
        model.model_json_schema()  # triggers same error
        print(f"✅ {model.__name__} OK")
    except Exception as e:
        print(f"❌ {model.__name__} FAILED: {e}")
        import traceback

        traceback.print_exc()
