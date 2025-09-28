from ....core import DbCore, ExceptionPackage

from .base import Category


def create(cls, category: Category) -> int:
    cls.__logger__.info(f"Creating new {cls.__name__}: {category}")
    query = f"INSERT INTO {cls.__table_name__} (name, description) VALUES (?, ?)"
    params = (category.name, category.description)
    exception_package = ExceptionPackage(
        unique_constraint_error=f"{cls.__name__} name '{category.name}' already exists"
    )
    last_row_id = DbCore.run_create(query, params, exception_package)
    category.id = last_row_id
    return last_row_id
