"""
Product Model - Product data structure and operations

This module is responsible for handling product data structures and data conversions.
"""


class Category:
    """
    Initialize Category instance

    Parameters:
        key (str): category key from json file
        name (str): category name
        description (str): category description
        ascii_art (str): category ascii art
    """
    def __init__(self, key: str, name: str, description: str, ascii_art: str):
        self.key = key
        self.name = name
        self.description = description
        self.ascii_art = ascii_art

    @staticmethod
    def from_dict(key: str, data: dict):
        """
        Convert from dictionary to object

        Parameters:
            key (str): category key from json file
            data (dict): category dict data

        Returns:
            Category: category object
        """
        return Category(
            key=key,
            name=data['name'],
            description=data['description'],
            ascii_art=data['ascii_art']
        )

class Product:
    """
    Initialize Product instance

    Parameters:
        product_id(str): product id from json file
        name (str): product name
        description (str): product description
        price (int): product price
        category (str): product category
        rarity (str): product rarity
    """
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
        """
        Convert from dictionary to object

        Parameters:
            data (dict): product dict data

        Returns:
            Product: product object
        """
        return Product(
            product_id=data['id'],
            name=data['name'],
            description=data['description'],
            price=data['price'],
            category=data['category'],
            rarity=data['rarity']
        )
