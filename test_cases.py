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

if __name__ == "__main__":
    test_catalog_operations()
    test_customer_operations()
    test_shopping_cart_operations()
    test_discount_application()
    test_invoice_generation()
