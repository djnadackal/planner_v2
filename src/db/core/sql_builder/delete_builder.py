import logging

from ..table_model import TableModel


logger = logging.getLogger(__name__)


def get_delete_query(table_model: TableModel) -> str:
    """Constructs the full SQL delete query."""
    pk_field = table_model.get_pk_fieldname()
    if not pk_field:
        raise ValueError(
            f"Table model '{table_model.__name__}' has no primary key fields"
        )
    query = (
        f"DELETE FROM {table_model.__table_name__} WHERE {pk_field} = ?;"
    )
    return query
