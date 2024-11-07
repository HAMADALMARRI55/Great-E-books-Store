# invoice.py

from discount import Discount
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