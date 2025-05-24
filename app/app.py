from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from app.actions.auth_action import AuthAction

class App:
    def __init__(self, console: Console, auth_action: AuthAction):
        self.console = console
        self.auth_action = auth_action
        self.current_user = None

    def main_menu(self):
        """Display the main menu and handle user input."""
        while True:
            self.console.clear()
            self.console.print(Panel(
                "[1] SIGN UP\n[2] SIGN IN\n[3] EXIT",
                title="LOGIN MENU",
            ))
            choice = Prompt.ask("Select an option", choices=["1", "2", "3"], default="3")

            if choice == "1":
                self.auth_action.handle_signup()
            elif choice == "2":
                user = self.auth_action.handle_signin()
                if user:
                    print(user)
                    self.current_user = user
                    self.authenticated_menu()
            elif choice == "3":
                self.console.print("Exiting CYBER TERMINAL SHOP. Goodbye.")
                break

    def authenticated_menu(self):
        """Display the authenticated menu for logged-in users."""
        while True:
            self.console.print(f"Welcome to CYBER TERMINAL SHOP {self.current_user.username}")


    def run(self):
        """Start the application."""
        self.console.print("Initializing CYBER TERMINAL SHOP...")
        self.main_menu()
