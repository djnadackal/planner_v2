from ..core import QueryBuilder


from typing import Type

from ..core import TableModel
from .actions import Action
from .categories import ActionType, ThingCategory, TicketCategory
from .things import Thing
from .tickets import Ticket
from .users import User


table_directory: dict[str, Type[TableModel]] = {
    "Thing": Thing,
    "ThingCategory": ThingCategory,
    "Ticket": Ticket,
    "TicketCategory": TicketCategory,
    "Action": Action,
    "ActionType": ActionType,
    "User": User,
}

QueryBuilder.table_directory = table_directory
