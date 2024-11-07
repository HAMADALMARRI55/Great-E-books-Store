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

    def remove_ebook(self, ebook):
        """
        Removes an EBook from the catalog.
        """
        if ebook in self.__ebooks:
            self.__ebooks.remove(ebook)

    @property
    def ebooks(self):
        """
        Returns the list of e-books in the catalog.
        """
        return self.__ebooks

    def __str__(self):
        """
        Returns a string representation of the Catalog.
        """
        return f"Catalog with {len(self.__ebooks)} e-books."
