"""Auth action - console authentication actions"""


from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from model.user import User
from service.auth_service import AuthService

class AuthAction:
    def __init__(self, console: Console, auth_service: AuthService):
        self.auth_service = auth_service
        self.console = console

    def handle_signup(self):
        """Handle user signup process."""
        self.console.clear()
        self.console.print(Panel(
            "=== SIGN UP ===",
            style="bright_cyan",
            border_style="bold magenta"
        ))

        while True:
            username = Prompt.ask("Enter username").lower()

            try:
                success, message = self.auth_service.register_user(username)
                if success:
                    Prompt.ask(f"{message}")
                    return

                self.console.print(f"Error: {message}\n", style="bold bright_red")
            except Exception as e:
                self.console.print(f"Error: {str(e)}\n", style="bold bright_red")

    def handle_signin(self) -> User | None:
        """Handle user signin process."""
        self.console.clear()
        self.console.print(Panel(
            "=== SIGN IN ===",
            style = "bright_cyan",
            border_style = "bold magenta"
        ))

        while True:
            username = Prompt.ask("Enter username").lower().strip()

            if len(username) < 7:
                self.console.print(f"Error: username must be at least 7 characters long.\n", style="bold bright_red")
                continue

            try:
                success, message, user = self.auth_service.authenticate_user(username)
                if success:
                    return user

                self.console.print(f"Error: {message}\n", style="bold bright_red")
            except Exception as e:
                self.console.print(f"Error: {str(e)}\n", style="bold bright_red")