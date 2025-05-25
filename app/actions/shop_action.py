"""
Shop Action - console shop actions

This module is responsible for handling shop based console actions.
"""

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table

from model.product import Category, Product
from service.shop_service import ShopService


class ShopAction:
    """
        Initialize Shop action instance

        Parameters:
            console (Console): Console instance from rich package
            shop_service (ShopService): Shop service for handling shop actions
        """
    def __init__(self, console: Console, shop_service: ShopService):
        self.shop_service = shop_service
        self.console = console

    def show_categories(self) -> list[Category]:
        """
        Displays categories.

        Returns:
             list[Category]: List of categories
        """
        try:
            categories = self.shop_service.get_categories()
        except Exception as e:
            self.console.print(f"Error: {str(e)}\n", style="bold bright_red")
            return []

        category_texts = ["[0] EXIT"]
        for idx, category in enumerate(categories):
            header_text = Text()
            header_text.append(f"[{idx+1}] ")
            header_text.append(f"{category.name} ")
            header_text.append(f"- {category.ascii_art}")

            category_texts.append(f"{header_text}\n{category.description}")

        self.console.print(Panel(
            "\n".join(str(text) for text in category_texts),
            title="PRODUCT CATEGORIES",
            style="bright_cyan",
            border_style="bold magenta"
        ))

        return categories

    def show_products(self, category_key: str) -> list[Product]:
        """
        Displays products in a category and return the list of products.

        Parameters:
            category_key (str): The category key for listing the products.

        Returns:
            list[Product]: List of products
        """
        try:
            products = self.shop_service.get_products_by_category(category_key)
        except Exception as e:
            self.console.print(f"Error: {str(e)}\n", style="bold bright_red")
            return []

        table = Table(show_header=False, style="dim cyan", border_style="bold magenta", expand=True)
        table.add_column("Option", style="bold bright_cyan", justify="left")
        table.add_column("Product", style="bold bright_green", justify="left")
        table.add_column("Rarity", style="bold bright_magenta", justify="center")
        table.add_column("Description", style="bright_white", justify="left")
        table.add_column("Price", style="bold bright_yellow", justify="right")

        table.add_row("[0]", "EXIT", "", "")

        rarity_styles = {
            "common": "dim white",
            "rare": "bold blue",
            "legendary": "bold bright_yellow"
        }

        rarity_symbols = {
            "common": "●",
            "rare": "◆",
            "legendary": "★"
        }

        for idx, product in enumerate(products):
            rarity_style = rarity_styles.get(product.rarity, "white")
            rarity_symbol = rarity_symbols.get(product.rarity, "●")

            table.add_row(
                f"[{idx + 1}]",
                product.name,
                f"[{rarity_style}]{rarity_symbol} {product.rarity.upper()}[/{rarity_style}]",
                product.description,
                f"{product.price} credits"
            )

        self.console.print("\n")
        self.console.print(Panel(
            table,
            title=f"PRODUCTS - {category_key.upper()}",
            style="bright_cyan",
            border_style="bold magenta",
            expand=True
        ))

        return products


