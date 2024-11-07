from datetime import date
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

# discount.py

class Discount:
    """
    Abstract base class for discounts.
    """

    def __init__(self, discount_rate):
        """
        Initializes a Discount with a discount rate.
        """
        self._discount_rate = discount_rate

    def is_applicable(self, order):
        """
        Determines if the discount is applicable to the order.
        Should be implemented by subclasses.
        """
        raise NotImplementedError("Must override is_applicable")

    def apply_discount(self, total):
        """
        Applies the discount to the total amount.
        """
        return total * (1 - self._discount_rate)

class LoyaltyDiscount(Discount):
    """
    Discount for loyalty program members.
    """

    def __init__(self):
        """
        Initializes a LoyaltyDiscount with a 10% discount rate.
        """
        super().__init__(0.10)

    def is_applicable(self, order):
        """
        Loyalty discount is applicable if the customer is a loyalty member.
        """
        # The order has an attribute to check loyalty status
        return getattr(order, 'is_loyalty_member', False)

class BulkPurchaseDiscount(Discount):
    """
    Discount for bulk purchases of 5 or more e-books.
    """

    def __init__(self):
        """
        Initializes a BulkPurchaseDiscount with a 20% discount rate.
        """
        super().__init__(0.20)

    def is_applicable(self, order):
        """
        Bulk discount is applicable if 5 or more e-books are purchased.
        """
        total_quantity = sum(order.items.values())
        return total_quantity >= 5

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

# test_cases.py

from ebook import EBook
from catalog import Catalog
from customer import Customer, LoyaltyMember
from shopping_cart import ShoppingCart
from order import Order
from invoice import Invoice
from discount import LoyaltyDiscount, BulkPurchaseDiscount


def test_catalog_operations():
    """
    Test adding and removing e-books in the catalog.
    """
    print("=== Test Catalog Operations ===")
    # Create a catalog
    catalog = Catalog()

    # Add an e-book to the catalog
    ebook1 = EBook("Learning Python", "Ahmed Al-Masri", "2020-05-01", "Programming", 30.00)
    catalog.add_ebook(ebook1)

    print("Catalog after adding an e-book:")
    for ebook in catalog.ebooks:
        print(ebook)

    # Remove the e-book
    catalog.remove_ebook(ebook1)
    print("Catalog after removing the e-book:")
    for ebook in catalog.ebooks:
        print(ebook)


def test_customer_operations():
    """
    Test adding and modifying customer accounts.
    """
    print("\n=== Test Customer Operations ===")
    # Add a customer
    customer1 = Customer("Fatima", "fatima@example.com")

    print("Customer added:")
    print(customer1)

    # Modify customer information
    customer1.contact_info = "fatima.new@example.com"
    print("Customer after updating contact info:")
    print(customer1)

    # Simulate removing a customer account
    customer1 = None
    print("Customer account removed.")


def test_shopping_cart_operations():
    """
    Test adding e-books to the shopping cart.
    """
    print("\n=== Test Shopping Cart Operations ===")
    # Create a customer
    customer = Customer("Omar", "omar@example.com")

    # Create an e-book
    ebook1 = EBook("Data Science Basics", "Leila Hassan", "2019-07-15", "Data Science", 25.00)

    # Add e-book to shopping cart
    customer.shopping_cart.add_item(ebook1, quantity=2)

    print("Shopping cart after adding an item:")
    for ebook, qty in customer.shopping_cart.items.items():
        print(f"{ebook} - Quantity: {qty}")


def test_discount_application():
    """
    Test applying discounts for loyalty program members.
    """
    print("\n=== Test Discount Application ===")
    # Create a loyalty member
    customer = LoyaltyMember("Sara", "sara@example.com")

    # Create an e-book
    ebook1 = EBook("Machine Learning", "Yusuf Ali", "2018-03-20", "Artificial Intelligence", 40.00)

    # Add e-book to shopping cart
    customer.shopping_cart.add_item(ebook1, quantity=1)

    # Create an order
    order = Order(customer.shopping_cart.items)
    order.is_loyalty_member = True  # Indicate customer is a loyalty member

    # Apply loyalty discount
    discounts = [LoyaltyDiscount()]
    invoice = Invoice(order, discounts)
    invoice.generate_invoice()

    print("Invoice for loyalty member:")
    print(f"Total Amount: {invoice.final_total:.2f}")


def test_invoice_generation():
    """
    Test the generation of an invoice.
    """
    print("\n=== Test Invoice Generation ===")
    # Create a customer
    customer = Customer("Hassan", "hassan@example.com")

    # Create an e-book
    ebook1 = EBook("Web Development", "Aisha Karim", "2021-01-10", "Programming", 35.00)

    # Add e-book to shopping cart
    customer.shopping_cart.add_item(ebook1, quantity=1)

    # Create an order
    order = Order(customer.shopping_cart.items)

    # No discounts applied
    invoice = Invoice(order)
    invoice.generate_invoice()

    print("Invoice for regular customer:")
    print(f"Total Amount: {invoice.final_total:.2f}")


def test_scenario_one():
    """
    Test Case 1: Full operation including all classes.
    """
    print("=== Test Scenario One ===")

    # Step 1: Create a catalog and add e-books
    catalog = Catalog()
    ebook1 = EBook("Introduction to AI", "Ali Hassan", "2021-06-01", "Technology", 50.00)
    ebook2 = EBook("Advanced Python", "Fatima Noor", "2020-09-15", "Programming", 40.00)
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)
    print("Catalog after adding e-books:")
    for ebook in catalog.ebooks:
        print(ebook)

    # Step 2: Modify an e-book's price
    ebook1.price = 45.00
    print("\nCatalog after modifying an e-book's price:")
    for ebook in catalog.ebooks:
        print(ebook)

    # Step 3: Remove an e-book from the catalog
    catalog.remove_ebook(ebook2)
    print("\nCatalog after removing an e-book:")
    for ebook in catalog.ebooks:
        print(ebook)

    # Step 4: Add a loyalty member customer
    customer = LoyaltyMember("Layla", "layla@example.com")
    print("\nCustomer account created:")
    print(customer)

    # Step 5: Modify customer information
    customer.contact_info = "layla.new@example.com"
    print("\nCustomer after updating contact info:")
    print(customer)

    # Step 6: Simulate removing customer account
    customer = None
    print("\nCustomer account removed.")

    # Recreate customer for further steps
    customer = LoyaltyMember("Layla", "layla.new@example.com")

    # Step 7: Add e-books to the shopping cart
    customer.shopping_cart.add_item(ebook1, quantity=5)
    print("\nShopping cart after adding items:")
    for ebook, qty in customer.shopping_cart.items.items():
        print(f"{ebook} - Quantity: {qty}")

    # Step 8: Create an order and apply discounts
    order = Order(customer.shopping_cart.items)
    order.is_loyalty_member = True  # Customer is a loyalty member
    discounts = [LoyaltyDiscount(), BulkPurchaseDiscount()]
    invoice = Invoice(order, discounts)
    invoice.generate_invoice()

    # Step 9: Generate and display invoice
    print("\nInvoice generated:")
    print(f"Total Amount (with discounts and VAT): {invoice.final_total:.2f}")


def test_scenario_two():
    """
    Test Case 2: Full operation including all classes.
    """
    print("\n=== Test Scenario Two ===")

    # Step 1: Create a catalog and add e-books
    catalog = Catalog()
    ebook1 = EBook("Basics of Data Science", "Omar Khalid", "2019-11-20", "Data Science", 30.00)
    ebook2 = EBook("Web Development Essentials", "Aisha Ahmed", "2021-02-10", "Technology", 35.00)
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)
    print("Catalog after adding e-books:")
    for ebook in catalog.ebooks:
        print(ebook)

    # Step 2: Modify an e-book's genre
    ebook2.genre = "Web Development"
    print("\nCatalog after modifying an e-book's genre:")
    for ebook in catalog.ebooks:
        print(ebook)

    # Step 3: Remove an e-book from the catalog
    catalog.remove_ebook(ebook1)
    print("\nCatalog after removing an e-book:")
    for ebook in catalog.ebooks:
        print(ebook)

    # Step 4: Add a regular customer
    customer = Customer("Yusuf", "yusuf@example.com")
    print("\nCustomer account created:")
    print(customer)

    # Step 5: Modify customer name
    customer.name = "Yusuf Ali"
    print("\nCustomer after updating name:")
    print(customer)

    # Step 6: Simulate removing customer account
    customer = None
    print("\nCustomer account removed.")

    # Recreate customer for further steps
    customer = Customer("Yusuf Ali", "yusuf@example.com")

    # Step 7: Add e-books to the shopping cart
    customer.shopping_cart.add_item(ebook2, quantity=4)
    print("\nShopping cart after adding items:")
    for ebook, qty in customer.shopping_cart.items.items():
        print(f"{ebook} - Quantity: {qty}")

    # Step 8: Create an order and apply discounts
    order = Order(customer.shopping_cart.items)
    order.is_loyalty_member = False  # Customer is not a loyalty member
    discounts = [BulkPurchaseDiscount()]  # Only bulk purchase discount applies
    invoice = Invoice(order, discounts)
    invoice.generate_invoice()

    # Step 9: Generate and display invoice
    print("\nInvoice generated:")
    print(f"Total Amount (with discounts and VAT): {invoice.final_total:.2f}")


if __name__ == "__main__":
    test_catalog_operations()
    test_customer_operations()
    test_shopping_cart_operations()
    test_discount_application()
    test_invoice_generation()
    test_scenario_one()
    test_scenario_two()
