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
