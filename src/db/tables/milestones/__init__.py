from ..util import as_classmethod, as_staticmethod

from .base import Milestone
from .params import MilestoneParams
from .create import create
from .update import update
from .get_by_id import get_by_id
from .read import read, ReadMilestonesResponse
from .delete import delete
from .from_row import from_row


setattr(Milestone, "create", create)
setattr(Milestone, "get_by_id", as_staticmethod(get_by_id))
setattr(Milestone, "read", as_staticmethod(read))
setattr(Milestone, "update", update)
setattr(Milestone, "delete", as_staticmethod(delete))
setattr(Milestone, "add_ticket", update)
setattr(Milestone, "remove_ticket", update)
setattr(Milestone, "from_row", as_classmethod(from_row))
Milestone.__params_class__ = MilestoneParams
Milestone.__table_name__ = "milestones"


__all__ = ["Milestone", "MilestoneParams", "ReadMilestonesResponse"]
