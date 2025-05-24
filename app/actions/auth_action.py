from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from model.user import User
from service.auth_service import AuthService

class AuthAction:
    def __init__(self, console: Console, auth_service: AuthService,):
        self.auth_service = auth_service
        self.console = console

    def handle_signup(self):
        """Handle user signup process."""
        self.console.clear()
        self.console.print(Panel("=== SIGN UP ==="))
        username = Prompt.ask("Enter username").lower()

        try:
            success, message = self.auth_service.register_user(username)
            if success:
                self.console.print(f"{message}")
                return

            self.console.print(f"Error: {message}")
        except Exception as e:
            self.console.print(f"Error: {str(e)}")

    def handle_signin(self) -> User | None:
        """Handle user signin process."""
        self.console.clear()
        self.console.print(Panel("=== SIGN IN ==="))
        username = Prompt.ask("Enter username").lower()

        try:
            success, message, user = self.auth_service.authenticate_user(username)
            if success:
                self.console.print(f"{message}")
                return user

            self.console.print(f"Error: {message}")
            return None
        except Exception as e:
            self.console.print(f"Error: {str(e)}")
            return None