from .category_base import Category, CategoryManager


# Pydantic model for Category
class TicketCategory(Category):
    pass


# Manager class for CRUD operations
class TicketCategoryManager(CategoryManager):
    __table_name__ = "ticket_categories"
    __category_model__ = TicketCategory
