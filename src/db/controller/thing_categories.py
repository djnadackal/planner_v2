from .category_base import Category, CategoryManager


# Pydantic model for Category
class ThingCategory(Category):
    pass


# Manager class for CRUD operations
class ThingCategoryManager(CategoryManager):
    __table_name__ = "thing_categories"
    __category_model__ = ThingCategory
