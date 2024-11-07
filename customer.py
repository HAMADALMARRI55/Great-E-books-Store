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
