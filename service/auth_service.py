"""
Auth Service - User authentication service
"""


import os
import uuid
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.dh import DHPrivateKey

from dao.data_manager import DataManager
from model.user import User

USER_FILE_PATH = "users.json"

class AuthService:
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager

    def register_user(self, username: str):
        """Register a new user with generated SSH key."""
        try:
            if len(username) < 7:
                return False, "Username should be at least 7 characters long."

            users = self.data_manager.load_json(USER_FILE_PATH)

            if username in users:
                return False, "Username already exists"

            private_key, public_key = self._generate_ssh_key()

            user_id = str(uuid.uuid4())  # Generate unique user_id
            user = User(username, public_key, user_id)

            users[username] = user.to_dict()
            self.data_manager.save_json(USER_FILE_PATH, users)

            self._save_private_key(username, private_key)

            return True, f"User {username} registered. Private key saved"
        except Exception as e:
            return False, f"Failed to register user {username}: {str(e)}"

    def authenticate_user(self, username: str) -> tuple[bool, str, User | None]:
        """Authenticate user with SSH key."""
        try:
            users = self.data_manager.load_json(USER_FILE_PATH)

            if username not in users:
                raise ValueError(f"User {username} not found")

            provided_private_key = self._load_private_key(username)

            provided_public_key = provided_private_key.public_key().public_bytes(
                encoding=serialization.Encoding.OpenSSH,
                format=serialization.PublicFormat.OpenSSH
            ).decode()

            if provided_public_key == users[username]["public_key"]:
                user = User.from_dict(users[username])
                return True, f"User {username} authenticated successfully", user
            else:
                raise ValueError("Invalid SSH key")
        except Exception as e:
            raise ValueError(f"Authentication failed: {str(e)}")

    def _generate_ssh_key(self) -> tuple[str, str]:
        """Generate SSH key."""
        try:
            key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )

            private_key = key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )

            public_key = key.public_key().public_bytes(
                encoding=serialization.Encoding.OpenSSH,
                format=serialization.PublicFormat.OpenSSH
            )

            return private_key.decode(), public_key.decode()
        except Exception as e:
            raise Exception(f"Failed to generate SSH key pair: {str(e)}")

    def _save_private_key(self, username: str, private_key: str):
        """Save private key to file."""
        try:
            private_key_path = os.path.join(self.data_manager.data_dir, f"{username}_private_key.pem")
            with open(private_key_path, "w") as f:
                f.write(private_key)
        except Exception as e:
            raise Exception(f"Failed to save private key: {str(e)}")

    def _load_private_key(self, username: str) -> DHPrivateKey:
        """Load private key from file."""
        try:
            private_key_path = os.path.join(self.data_manager.data_dir, f"{username}_private_key.pem")

            with open(private_key_path, "rb") as f:
                private_key = serialization.load_pem_private_key(
                    f.read(), password=None, backend=default_backend()
                )
            return private_key
        except FileNotFoundError:
            raise ValueError(f"Private key file not found: {private_key_path}")
        except Exception as e:
            raise ValueError(f"Failed to load private key: {str(e)}")