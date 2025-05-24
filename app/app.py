"""APP console"""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from app.actions.auth_action import AuthAction
from app.actions.shop_action import ShopAction


class App:
    def __init__(self, console: Console, auth_action: AuthAction, shop_action: ShopAction):
        self.console = console
        self.auth_action = auth_action
        self.shop_action = shop_action
        self.current_user = None
        self.state = "login"

    def login_menu(self):
        """Display the login menu and handle user input."""
        self.console.clear()
        self.console.print(Panel(
            "[1] SIGN UP\n[2] SIGN IN\n[3] EXIT",
            title="LOGIN MENU",
            style="cyan",
            border_style="purple"
        ))
        choice = Prompt.ask("Select an option", choices=["1", "2", "3"], default="3")

        if choice == "1":
            self.auth_action.handle_signup()
            self.state = "login"
        elif choice == "2":
            user = self.auth_action.handle_signin()
            if user:
                self.console.print(f"[bold green]Welcome, {user.username}! You are now signed in.[/bold green]")
                self.current_user = user
                self.state = "main"
        elif choice == "3":
            self.console.clear()
            self.console.print("[bold magenta]Exiting CYBER TERMINAL SHOP. Goodbye.[/bold magenta]")
            self.state = None

    def main_menu(self):
        """Display the authenticated menu for logged-in users."""
        self.console.clear()
        self.console.print(Panel(
            "[1] CATEGORIES\n[2] EXIT",
            title="MAIN MENU",
            style="cyan",
            border_style="purple"
        ))
        choice = Prompt.ask("Select an option", choices=["1", "2"], default="2")

        if choice == "1":
            self.categories_menu()
            self.state = "main"
        elif choice == "2":
            self.current_user = None
            self.state = "login"

    def categories_menu(self):
        self.console.clear()
        num_categories = self.shop_action.show_categories()

        choice_rng = [str(i) for i in range(0, num_categories + 1)]
        choice = Prompt.ask("Select a category", choices=choice_rng, default="0")

        if choice == "0":
            self.main_menu()
        if 0 < int(choice) < num_categories:
            self.product_menu()

    def product_menu(self):
        self.console.print("Working on it")

    def run(self):
        """Start the application."""
        self.console.print("[bold magenta]Initializing CYBER TERMINAL SHOP...[/bold magenta]")
        while self.state:
            if self.state == "login":
                self.login_menu()
            elif self.state == "main":
                self.main_menu()
