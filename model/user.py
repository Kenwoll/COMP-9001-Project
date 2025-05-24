"""
User Model - User data structure and operations
"""


class User:
    def __init__(self, username, ssh_public_key, user_id):
        self.username = username
        self.ssh_public_key = ssh_public_key
        self.user_id = user_id

    def to_dict(self):
        """Convert to dictionary for JSON storage"""
        return {
            "username": self.username,
            "public_key": self.ssh_public_key,
            "user_id": self.user_id,
            "orders": []
        }