import datetime

# Exchange rates (fixed, EUR as base currency, based on the exchange rates on the 24th of February 2025)
exchange_rates = {
    "EUR": 1.0,  # Base currency (Euro)
    "USD": 1.045,  # 1 EUR = 1.045 USD
    "GBP": 0.83,  # 1 EUR = 0.83 GBP
    "JPY": 162.5,  # 1 EUR = 162.5 JPY
    "AUD": 1.64,  # 1 EUR = 1.64 AUD
    "CAD": 1.48  # 1 EUR = 1.48 CAD
}


def get_exchange_rate(currency):
    """Returns the exchange rate for a given currency relative to EUR."""
    return exchange_rates.get(currency.upper(), None)


def convert_currency(amount, rate):
    """Converts amount from EUR to target currency using exchange rate."""
    return amount / rate


def calculate_savings_needed(trip_cost, savings, monthly_savings):
    """Calculates time needed to save for the trip."""
    remaining_amount = trip_cost - savings
    if remaining_amount <= 0:
        return 0  # Already saved enough
    months_needed = round(remaining_amount / monthly_savings, 1)
    return months_needed


def suggest_faster_savings(time_needed, monthly_savings):
    """Suggests alternative savings plans to reach the goal faster."""
    print("\nWant to reach your savings goal faster? Consider these options:")
    for extra in [50, 100, 200]:  # Testing extra savings amounts
        new_savings = monthly_savings + extra
        new_time = round((time_needed * monthly_savings) / new_savings, 1)
        print(f"- If you save €{new_savings} per month, you'll reach your goal in {new_time} months!")



def display_summary(destination, trip_budget, local_currency, time_needed, savings, trip_cost_in_eur):
    """Displays final savings plan and estimated travel date."""
    today = datetime.date.today()
    estimated_date = today + datetime.timedelta(days=30 * time_needed)

