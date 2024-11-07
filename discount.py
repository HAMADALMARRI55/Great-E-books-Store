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
