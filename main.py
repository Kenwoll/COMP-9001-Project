from rich.console import Console

from app.actions.auth_action import AuthAction
from app.actions.shop_action import ShopAction
from app.app import App
from dao.data_manager import DataManager
from service.auth_service import AuthService
from service.shop_service import ShopService

if __name__ == '__main__':
    console = Console()
    data_manager = DataManager()

    auth_service = AuthService(data_manager)
    shop_service = ShopService(data_manager)

    auth_action = AuthAction(console, auth_service)
    shop_action = ShopAction(console, shop_service)

    app = App(console, auth_action, shop_action)

    app.run()