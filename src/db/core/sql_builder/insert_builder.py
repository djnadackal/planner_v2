from typing import Optional, Type
import logging

from ..query_params import QueryParams
from ..table_model import TableModel


logger = logging.getLogger(__name__)


class InsertBuilder:
    """A class initialized with a table model that dynamically builds SQL insert queries."""

    table_directory: dict[str, Type[TableModel]] = {}

    def __init__(
        self,
        table_model: TableModel,
    ):
        self.table_model = table_model

    @property
    def query(self) -> tuple[str, tuple]:
        """Constructs the full SQL insert query."""
        columns = []
        placeholders = []
        values = ()
        for field_name, field in self.table_model.get_column_fields(
            exclude_pk=True
        ).items():
            value = getattr(self.table_model, field_name)
            if value is None and not field.json_schema_extra.get(
                "nullable", True
            ):
                raise ValueError(f"Field '{field_name}' cannot be None")
            if value is not None:
                columns.append(field_name)
                placeholders.append("?")
                values += (value,)
        columns_str = ", ".join(columns)
        placeholders_str = ", ".join(placeholders)
        query = f"INSERT INTO {self.table_model.__table_name__} ({columns_str}) VALUES ({placeholders_str});"
        return query, values
