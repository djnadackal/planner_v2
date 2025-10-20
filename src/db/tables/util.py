from functools import wraps
from pydantic import Field


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


class OrmField(Field):
    """
    A Pydantic Field subclass that indicates the field is intended for ORM use.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra["orm_field"] = True
