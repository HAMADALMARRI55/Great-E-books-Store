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