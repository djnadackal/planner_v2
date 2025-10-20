class QueryBuilder:
    """A class initialized with a table model that dynamically builds SQL queries."""

    def __init__(self, table_model):
        self.table_model = table_model
