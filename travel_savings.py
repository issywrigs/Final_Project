import datetime

# Exchange rates (fixed, USD as base currency, based on the exchange rates on the 24th of February 2025)
exchange_rates = { "USD": 1.0, "EUR": 0.9563, "GBP": 0.7915, "JPY": 149.2736, "AUD": 1.5708,"CAD": 1.4225 }

def get_exchange_rate(currency):
    """Returns the exchange rate for a given currency."""
    return exchange_rates.get(currency.upper(), None)

def convert_currency(amount, rate):
    """Converts amount using exchange rate."""
    return amount / rate

def calculate_savings_needed(trip_cost, savings, monthly_savings):
    """Calculates time needed to save for the trip."""
    remaining_amount = trip_cost - savings
    if remaining_amount <= 0:
        return 0  # Already saved enough
    months_needed = round(remaining_amount / monthly_savings, 1)
    return months_needed

def display_summary(destination, trip_budget, local_currency, time_needed):
    """Displays final savings plan and estimated travel date."""
    today = datetime.date.today()
    estimated_date = today + datetime.timedelta(days=30 * time_needed)

    print("\n--- Travel Savings Summary ---")
    print(f"Destination: {destination}")
    print(f"Trip Cost in {local_currency}: {trip_budget:,.2f}")
    print(f"Time needed to save: {time_needed} months")
    print(f"Estimated travel-ready date: {estimated_date.strftime('%B %Y')}")
    if time_needed > 0:
        print("Tip: Increase monthly savings to reach your goal sooner!")


# Main program
print("Welcome to the Travel Savings & Currency Converter! Find out how long you need to save for your trip!\n")

# Check if they are travelling to a country supported by our currency converter and end the program if not
print("Are you planning to travel to the EU, UK, Japan, Australia, or Canada?")
travel_plan = input("Type 'yes' or 'no': ")

if travel_plan == "yes":
    print("That’s exciting! Let’s continue planning your trip.\n")
elif travel_plan == "no":
    print("Unfortunately, this converter only supports certain destinations at the moment.")
    print("We hope you enjoy your trip, and feel free to come back in the future!")
    exit()  # Exits the program

try:
    destination = input("Enter your destination country: ")
    local_currency = input("Enter the currency for this destination (JPY, EUR, GBP, CAD, AUD): ").upper()

    exchange_rate = get_exchange_rate(local_currency)
    if exchange_rate is None:
        print("Sorry, this currency is not supported. Please restart the program and enter a valid currency.")
    else:
        trip_budget = float(input(f"Enter your estimated trip budget in {local_currency}: "))
        savings = float(input("Enter your current savings in your home currency (USD): "))
        monthly_savings = float(input("Enter your monthly savings amount (USD): "))

    trip_cost_in_usd = convert_currency(trip_budget, exchange_rate)
    time_needed = calculate_savings_needed(trip_cost_in_usd, savings, monthly_savings)

    display_summary(destination, trip_budget, local_currency, time_needed)

except ValueError:
    print("Error: Please enter valid numerical values.")