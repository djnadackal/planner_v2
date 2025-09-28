from .tables import Controller
from .core import DbCore


# initialize the database core to ensure
# the database and tables are created
Core = DbCore()


__all__ = ["Controller", "DbCore"]
