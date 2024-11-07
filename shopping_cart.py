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

    def add_item(self, ebook, quantity=1):
        """
        Adds an e-book to the cart.
        """
        if isinstance(ebook, EBook):
            if ebook in self.__items:
                self.__items[ebook] += quantity
            else:
                self.__items[ebook] = quantity

    def remove_item(self, ebook):
        """
        Removes an e-book from the cart.
        """
        if ebook in self.__items:
            del self.__items[ebook]

    def update_quantity(self, ebook, quantity):
        """
        Updates the quantity of an e-book in the cart.
        """
        if ebook in self.__items:
            self.__items[ebook] = quantity

    @property
    def items(self):
        """
        Returns the items in the shopping cart.
        """
        return self.__items

    def __str__(self):
        """
        Returns a string representation of the ShoppingCart.
        """
        return f"ShoppingCart with {len(self.__items)} items."
