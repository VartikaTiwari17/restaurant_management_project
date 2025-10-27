from decimal import Decimal, ROUND_HALF_UP

def calculate_sales_tax(amount: Decimal, tax_rate: Decimal) -> Decimal:
    """
    Calculate and return the sales tax amount.

    Parameters:
        amount (Decimal): Subtotal before tax.
        tax_rate (Decimal): Tax rate as a decimal (e.g., 0.08 for 8%).

    Returns:
        Decimal: The calculated sales tax.
    """
    if not isinstance(amount, Decimal) or not isinstance(tax_rate, Decimal):
        raise TypeError("Both amount and tax_rate must be of type Decimal.")

    tax = (amount * tax_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return tax
