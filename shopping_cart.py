# shopping_cart.py

from ebook import EBook

class ShoppingCart:
    """
    Represents a shopping cart containing e-books.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.__items = {}
