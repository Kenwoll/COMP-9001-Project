"""
Order Model - Order data structure and operations
"""


class Order:
    def __init__(self, order_id, username, items, total_price, status="pending"):
        self.order_id = order_id
        self.username = username
        self.items = items
        self.total_price = total_price
        self.status = status

    def to_dict(self):
        """Convert to dictionary for JSON storage"""
        pass