"""Shop Action - console actions for shop or products"""


from rich.console import Console
from rich.text import Text
from rich.panel import Panel

from service.shop_service import ShopService

class ShopAction:
    def __init__(self, console: Console, shop_service: ShopService):
        self.shop_service = shop_service
        self.console = console

    def show_categories(self) -> int:
        categories = self.shop_service.get_categories()

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
            style="cyan",
            border_style="purple"
        ))

        return len(categories)