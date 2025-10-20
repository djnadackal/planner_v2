from pydantic import BaseModel


class QueryBuilder:
    """A class initialized with a table model that dynamically builds SQL queries."""

    def __init__(self, table_model):
        self.table_model = table_model
        self.select = ""
        self.where = ""
        self.join = ""

    @property
    def table_name(self):
        """The table name is just the class name in lower snake case"""
        return self.table_model.__table_name__

    @property
    def 

    def build_query(self, params: BaseModel):
        # first build select, using the table model's fields and the include fields
        # from the params
        # then add any joins necessated by the include options in params
        # finally, add where clauses based on params
