# catalog.py

from ebook import EBook

class Catalog:
    """
    Manages a collection of EBook instances.
    """

    def __init__(self):
        """
        Initializes the Catalog with an empty list of e-books.
        """
        self.__ebooks = []

    def add_ebook(self, ebook):
        """
        Adds an EBook to the catalog.
        """
        if isinstance(ebook, EBook):
            self.__ebooks.append(ebook)
