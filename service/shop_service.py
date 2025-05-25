"""
Shop Service - Handles product catalog and shopping cart operations
"""

from dao.data_manager import DataManager
from model.product import Product, Category


PRODUCTS_FILE_PATH = "products.json"


class ShopService:
    """
    Initialize Shop Service instance

    Parameters:
        data_manager (DataManager): data manager instance
    """
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def get_categories(self) -> list[Category]:
        """
        Get all product categories

        Returns:
            list[Category]: all product categories
        """
        try:
            categories = self.data_manager.load_json(PRODUCTS_FILE_PATH)["categories"]
            categories = [Category.from_dict(key, cat) for key, cat in categories.items()]

            return categories
        except Exception as e:
            raise ValueError(f"Failed to load categories: {str(e)}")

    def get_products_by_category(self, category: str) -> list[Product]:
        """
        Get products in a specific category.

        Parameters:
            category (str): category name

        Returns:
            list[Product]: all products in a specific category
        """
        try:
            products = self.data_manager.load_json(PRODUCTS_FILE_PATH)["products"]
            products = [Product.from_dict(p) for p in products]
            products = filter(lambda p: p.category == category, products)

            return list(products)
        except Exception as e:
            raise ValueError(f"Failed to load products for category '{category}': {str(e)}")