# app.py (or wherever you create FastAPI app)
from fastapi import FastAPI
from pydantic import BaseModel
import inspect
from src.db.tables import (
    UserParams,
)

app = FastAPI()

try:
    print(UserParams.model_json_schema())  # triggers same error
    print(f"✅ {UserParams.__name__} OK")
except Exception as e:
    print(f"❌ {UserParams.__name__} FAILED: {e}")
    import traceback

    traceback.print_exc()
