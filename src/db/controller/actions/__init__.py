from functools import wraps
import logging

from ...core import DbCore

from .base import Action
from .create import create
from .get_by_id import get_by_id
from .read import read_actions
from .update import update
from .delete import delete
from .from_row import from_row
from .params import ActionParams


logger = logging.getLogger(__name__)

DbCore.logger = logger


def as_staticmethod(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return staticmethod(wrapper)


def as_classmethod(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return classmethod(wrapper)


# attach CRUD functions to Action class
setattr(Action, "create", create)
setattr(Action, "get_by_id", as_staticmethod(get_by_id))
setattr(Action, "read", as_staticmethod(read_actions))
setattr(Action, "update", update)
setattr(Action, "delete", as_staticmethod(delete))
setattr(Action, "from_row", as_staticmethod(from_row))


__all__ = ["Action", "ActionParams"]
