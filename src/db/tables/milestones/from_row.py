from .base import Milestone


def from_row(cls, **row) -> Milestone:
    ticket = cls(
        id=row["id"],
        name=row["name"],
        description=row["description"],
        due_date=row["due_date"],
    )
    return ticket
