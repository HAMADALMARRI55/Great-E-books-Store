# ebook.py

class EBook:
    """
    Represents an e-book with detailed information.
    """

    def __init__(self, title, author, publication_date, genre, price):
        """
        Initializes an EBook instance.
        """
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getter and Setter for title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    # Getter and Setter for author
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    # Getter and Setter for publication_date
    @property
    def publication_date(self):
        return self.__publication_date

    @publication_date.setter
    def publication_date(self, value):
        self.__publication_date = value

    # Getter and Setter for genre
    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    # Getter and Setter for price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        """
        Returns a string representation of the EBook.
        """
        return f"EBook(title={self.title}, author={self.author}, price={self.price})"


# catalog.py
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


# catalog.py
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
