# customer.py

from shopping_cart import ShoppingCart

class Customer:
    """
    Represents a customer with personal details and actions.
    """

    def __init__(self, name, contact_info):
        """
        Initializes a Customer instance.
        """
        self.__name = name
        self.__contact_info = contact_info
        self.__shopping_cart = ShoppingCart()
        self.__orders = []
