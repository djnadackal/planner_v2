from .controller import *
from .views import *


class database:
    controller = controller
    views = views


from .util import initialize_db


initialize_db()
