"""
User Model - User data structure and operations
"""


class User:
    def __init__(self, username, public_key, user_id):
        self.username = username
        self.public_key = public_key
        self.user_id = user_id

    def to_dict(self) -> dict:
        """
        Convert to dictionary for JSON storage

        Returns:
            dict: dictionary representation of user
        """
        return {
            "username": self.username,
            "public_key": self.public_key,
            "user_id": self.user_id,
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Convert from dictionary to object

        Parameters:
            data (dict): user dict data

        Returns:
            User: user object
        """
        return User(
            username=data["username"],
            public_key=data["public_key"],
            user_id=data["user_id"])
