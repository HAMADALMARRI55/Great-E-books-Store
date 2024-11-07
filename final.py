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


# customer.py

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

    # Getter and Setter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Getter and Setter for contact_info
    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        self.__contact_info = value

    @property
    def shopping_cart(self):
        """
        Returns the customer's shopping cart.
        """
        return self.__shopping_cart

    @property
    def orders(self):
        """
        Returns the list of orders placed by the customer.
        """
        return self.__orders

    def place_order(self, order):
        """
        Adds an order to the customer's order history.
        """
        self.__orders.append(order)

    def __str__(self):
        """
        Returns a string representation of the Customer.
        """
        return f"Customer(name={self.name}, contact_info={self.contact_info})"

class LoyaltyMember(Customer):
    """
    Represents a customer who is a loyalty program member.
    """

    def __init__(self, name, contact_info):
        """
        Initializes a LoyaltyMember instance.
        """
        super().__init__(name, contact_info)
        self.__loyalty_discount = 0.10  # 10% discount

    @property
    def loyalty_discount(self):
        """
        Returns the loyalty discount rate.
        """
        return self.__loyalty_discount

    def __str__(self):
        """
        Returns a string representation of the LoyaltyMember.
        """
        return f"LoyaltyMember(name={self.name}, discount={self.loyalty_discount})"

# shopping_cart.py

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


# invoice.py

from datetime import date

class Invoice:
    """
    Represents an invoice generated from an order.
    """

    def __init__(self, order, discounts=[]):
        """
        Initializes an Invoice with an order and optional discounts.
        """
        self.__order = order
        self.__discounts_applied = discounts
        self.__vat_rate = 0.08  # 8% VAT
        self.__final_total = 0.0

    def generate_invoice(self):
        """
        Generates the invoice, applying discounts and VAT.
        """
        total = self.__order.calculate_total()

        # Apply discounts
        for discount in self.__discounts_applied:
            if discount.is_applicable(self.__order):
                total = discount.apply_discount(total)

        # Apply VAT
        vat_amount = total * self.__vat_rate
        self.__final_total = total + vat_amount

    @property
    def final_total(self):
        """
        Returns the final total after discounts and VAT.
        """
        return self.__final_total

    def __str__(self):
        """
        Returns a string representation of the Invoice.
        """
        return f"Invoice(total={self.final_total})"
