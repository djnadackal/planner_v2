from pydantic import BaseModel, Field


class QueryParams(BaseModel):
    """
    Base class for query parameter models.
    """

    @classmethod
    def get_filter_params(cls) -> dict[str, Field]:
        return {
            field_name: field
            for field_name, field in cls.__fields__.items()
            if field.json_schema_extra
            and field.json_schema_extra.get("filter_param", False)
        }

    @property
    def pagination(self) -> str:
        """Constructs the pagination clause for SQL queries."""
        page_number = getattr(self, "page_number", None)
        page_size = getattr(self, "page_size", None)
        if page_number is not None and page_size is not None:
            offset = (page_number - 1) * page_size
            return f"LIMIT {page_size} OFFSET {offset}"
        return ""
