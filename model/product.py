"""
Product Model - Product data structure and operations
"""

class Category:
    def __init__(self, name: str, description: str, ascii_art: str) -> None:
        self.name = name
        self.description = description
        self.ascii_art = ascii_art

    @staticmethod
    def from_dict(data: dict):
        """Convert to dictionary to object"""
        return Category(
            name=data['name'],
            description=data['description'],
            ascii_art=data['ascii_art']
        )

class Product:
    def __init__(self, product_id: str, name: str, description: str, price: int,
                 category: str, rarity: str | None = None):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.rarity = rarity

    @staticmethod
    def from_dict(data: dict):
        """Convert to dictionary to object"""
        return Product(
            product_id=data['id'],
            name=data['name'],
            description=data['description'],
            price=data['price'],
            category=data['category'],
            rarity=data['rarity']
        )
