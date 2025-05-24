from rich.console import Console

from app.actions.auth_action import AuthAction
from app.app import App
from dao.data_manager import DataManager
from service.auth_service import AuthService

if __name__ == '__main__':
    console = Console()
    data_manager = DataManager()
    auth_service = AuthService(data_manager)
    auth_action = AuthAction(console, auth_service)

    app = App(console, auth_action)

    app.run()