from .categories import (
    CategoryParams,
    ThingCategory,
    TicketCategory,
    ActionType,
)
from .actions import Action, ActionParams
from .comments import Comment, CommentParams
from .things import Thing, ThingParams
from .tickets import Ticket, TicketParams


Thing.model_rebuild()
Ticket.model_rebuild()
Action.model_rebuild()


class Controller:
    class Tables:
        Thing = Thing
        ThingCategory = ThingCategory
        Ticket = Ticket
        TicketCategory = TicketCategory
        Comment = Comment
        Action = Action
        ActionType = ActionType

    class Params:
        Thing = ThingParams
        Ticket = TicketParams
        Category = CategoryParams
        Comment = CommentParams
        Action = ActionParams
