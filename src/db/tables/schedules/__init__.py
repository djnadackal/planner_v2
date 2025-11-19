from ..util import as_staticmethod

from .base import Schedule
from .params import ScheduleParams
from .create import create
from .update import update
from .get_by_id import get_by_id
from .read import read, ReadSchedulesResponse
from .delete import delete


setattr(Schedule, "create", create)
setattr(Schedule, "get_by_id", as_staticmethod(get_by_id))
setattr(Schedule, "read", as_staticmethod(read))
setattr(Schedule, "update", update)
setattr(Schedule, "delete", as_staticmethod(delete))
setattr(Schedule, "add_ticket", update)
setattr(Schedule, "remove_ticket", update)
Schedule.__params_class__ = ScheduleParams
Schedule.__table_name__ = "schedules"


__all__ = ["Schedule", "ScheduleParams", "ReadSchedulesResponse"]
