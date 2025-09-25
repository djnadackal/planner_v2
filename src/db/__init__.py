from .controller import *
from .views import *
from .core import DbCore


class database:
    controller = controller
    views = views
    # initialize the database core to ensure
    # the database and tables are created
    core = DbCore()
