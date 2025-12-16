from typing import Type
import logging

from ..table_model import TableModel


logger = logging.getLogger(__name__)


def get_ddl_query(table_model: Type[TableModel]) -> str:
    """Constructs the full SQL DDL query for creating a table."""
    columns = []
    for field_name, field in table_model.get_column_fields().items():
        column_def = f"{field_name} {field.get_sql_type()}"
        if field.is_primary_key:
            column_def += " PRIMARY KEY"
        if not field.json_schema_extra.get("nullable", True):
            column_def += " NOT NULL"
        columns.append(column_def)
    columns_str = ", ".join(columns)
    query = f"CREATE TABLE IF NOT EXISTS {table_model.__table_name__} ({columns_str});"
    return query
