"""
Shop Service - Handles product catalog and shopping cart operations
"""


from dao.data_manager import DataManager
from model.product import Product, Category

PRODUCTS_FILE_PATH = "products.json"

class ShopService:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def get_categories(self) -> list[Category]:
        """Get all product categories"""
        try:
            categories = self.data_manager.load_json(PRODUCTS_FILE_PATH)["categories"]
            categories = [Category.from_dict(cat) for _, cat in categories.items()]
            return categories
        except Exception as e:
            raise ValueError(f"Failed to load categories: {str(e)}")

    def get_products_by_category(self, category: str) -> list[Product]:
        """Get products in a specific category."""
        try:
            categories = self.data_manager.load_json(PRODUCTS_FILE_PATH)
            if category not in categories:
                raise ValueError(f"Category '{category}' not found")
            return categories.get(category, [])
        except Exception as e:
            raise ValueError(f"Failed to load products for category '{category}': {str(e)}")