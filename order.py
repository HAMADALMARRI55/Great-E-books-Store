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

    @property
    def order_date(self):
        """
        Returns the order date.
        """
        return self.__order_date

    @property
    def items(self):
        """
        Returns the items in the order.
        """
        return self.__items

    @property
    def total_amount(self):
        """
        Returns the total amount of the order.
        """
        return self.__total_amount

    def calculate_total(self):
        """
        Calculates the total amount of the order.
        """
        self.__total_amount = sum(ebook.price * qty for ebook, qty in self.__items.items())
        return self.__total_amount

    def __str__(self):
        """
        Returns a string representation of the Order.
        """
        return f"Order(date={self.order_date}, total_amount={self.total_amount})"
