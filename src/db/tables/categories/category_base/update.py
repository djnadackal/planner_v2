from ....core import DbCore, ExceptionPackage

from .base import Category


def update(cls, category: Category) -> None:
    cls.__logger__.info(f"Updating {cls.__name__}: {category}")
    if category.id is None:
        raise ValueError(f"{cls.__name__} ID is required for update")
    query = f"UPDATE {cls.__table_name__} SET name = ?, description = ? WHERE id = ?"
    params = (category.name, category.description, category.id)
    exception_package = ExceptionPackage(
        unique_constraint_error=f"{cls.__name__} name '{category.name}' already exists",
        not_found_error=f"{cls.__name__} with ID {category.id} not found",
    )
    DbCore.run_update(query, params, exception_package)
