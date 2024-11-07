# order.py

from datetime import date

class Order:
    """
    Represents a customer's order.
    """

    def __init__(self, items):
        """
        Initializes an Order with items and the current date.
        """
        self.__order_date = date.today()
        self.__items = items  # Should be a dictionary of EBook to quantity
        self.__total_amount = 0.0