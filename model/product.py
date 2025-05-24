"""
Product Model - Product data structure and operations
"""


class Product:
    def __init__(self, product_id, name, description, price, category, rarity=None):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.rarity = rarity

    def to_dict(self):
        """Convert to dictionary for JSON storage"""
        pass