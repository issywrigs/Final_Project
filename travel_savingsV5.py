import datetime

# Exchange rates (fixed, EUR as base currency, based on the exchange rates on the 24th of February 2025)
exchange_rates = {
    "EUR": 1.0,
    "USD": 1.045,
    "GBP": 0.83,
    "JPY": 162.5,
    "AUD": 1.64,
    "CAD": 1.48
}

# Weather data (Average monthly temperatures in °C for each country)
weather_data = {
    "USA": {"Jan": 2, "Feb": 3, "Mar": 8, "Apr": 12, "May": 18, "Jun": 24, "Jul": 28, "Aug": 27, "Sep": 22, "Oct": 15,
            "Nov": 9, "Dec": 4},
    "UK": {"Jan": 5, "Feb": 6, "Mar": 9, "Apr": 12, "May": 16, "Jun": 19, "Jul": 22, "Aug": 21, "Sep": 18, "Oct": 13,
           "Nov": 9, "Dec": 6},
    "JAPAN": {"Jan": 5, "Feb": 6, "Mar": 10, "Apr": 15, "May": 20, "Jun": 23, "Jul": 27, "Aug": 29, "Sep": 25,
              "Oct": 19, "Nov": 13, "Dec": 8},
    "AUSTRALIA": {"Jan": 26, "Feb": 25, "Mar": 23, "Apr": 19, "May": 16, "Jun": 14, "Jul": 12, "Aug": 13, "Sep": 16,
                  "Oct": 19, "Nov": 22, "Dec": 25},
    "CANADA": {"Jan": -5, "Feb": -3, "Mar": 2, "Apr": 10, "May": 16, "Jun": 21, "Jul": 25, "Aug": 24, "Sep": 18,
               "Oct": 11, "Nov": 4, "Dec": -2},
    "EU": {"Jan": 2, "Feb": 4, "Mar": 9, "Apr": 14, "May": 18, "Jun": 22, "Jul": 25, "Aug": 26, "Sep": 21, "Oct": 15,
           "Nov": 9, "Dec": 4},
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
        return 0
    months_needed = round(remaining_amount / monthly_savings, 1)
    return months_needed


def get_travel_month(time_needed):
    """Returns the estimated travel month in abbreviated format."""
    today = datetime.date.today()
    estimated_date = today + datetime.timedelta(days=30 * time_needed)
    return estimated_date.strftime('%b %Y')  # '%b' gives a 3-letter month abbreviation


def suggest_packing_list(destination, travel_month):
    """Suggests a packing list based on expected weather."""
    month_abbr = travel_month.split()[0]

    destination = destination.upper()

    if destination in weather_data and month_abbr in weather_data[destination]:
        avg_temp = weather_data[destination][month_abbr]

        print("\n--- Packing Recommendations Based on Weather ---")
        print(f"Expected temperature in {destination} during {travel_month}: {avg_temp}°C")

        packing_list = ["Passport", "Travel Insurance", "Phone & Charger", "Toiletries"]

        if avg_temp <= 5:
            packing_list += ["Heavy Jacket", "Gloves", "Scarf", "Thermal Wear"]
            print("It will be **cold**! Pack winter clothing. ❄")
        elif 6 <= avg_temp <= 18:
            packing_list += ["Sweater", "Comfortable Jeans", "Rain Jacket"]
            print("It will be **mild**! Pack layered clothing. 🍂")
        else:
            packing_list += ["Sunglasses", "Sunscreen", "Light Clothing", "Swimwear"]
            print("It will be **warm**! Pack for summer weather. ☀")

        print("\nRecommended Packing List:")
        for item in packing_list:
            print(f"- {item}")


def suggest_faster_savings(time_needed, monthly_savings):
    """Suggests alternative savings plans."""
    print("\nWant to reach your savings goal faster? Consider these options:")
    for extra in [50, 100, 200]:
        new_savings = monthly_savings + extra
        new_time = round((time_needed * monthly_savings) / new_savings, 1)
        print(f"- If you save €{new_savings} per month, you'll reach your goal in {new_time} months!")


# Main program
print("Welcome to the Travel Savings & Currency Converter!")

holiday_plan = input("\nAre you planning to go on holiday? (yes/no): ").strip().lower()
if holiday_plan == "no":
    print("\nWe hope you plan a trip soon! Restart the program if you change your mind. 😊")
    exit()

print("\nFind out how long you need to save for your trip!\n")

print("Are you planning to travel to the USA, EU, UK, Japan, Australia, or Canada?")
travel_plan = input("Type 'yes' or 'no': ").strip().lower()
if travel_plan == "no":
    print("Unfortunately, this converter only supports certain destinations.")
    exit()

try:
    destination = input("Enter your destination country: ").strip().upper()
    local_currency = input("Enter the currency for this destination (JPY, EUR, GBP, CAD, AUD, USD): ").strip().upper()

    exchange_rate = get_exchange_rate(local_currency)
    if exchange_rate is None:
        print("Sorry, this currency is not supported.")
        exit()

    print("\nLet's break down your trip budget:")
    flight_cost = float(input(f"Enter your estimated flight cost in {local_currency}: "))
    hotel_cost = float(input(f"Enter your estimated hotel cost in {local_currency}: "))
    food_cost = float(input(f"Enter your estimated food cost in {local_currency}: "))
    activity_cost = float(input(f"Enter your estimated activity cost in {local_currency}: "))

    trip_budget = flight_cost + hotel_cost + food_cost + activity_cost
    savings = float(input("\nEnter your current savings in EUR: "))
    monthly_savings = float(input("Enter your monthly savings amount in EUR: "))

    trip_cost_in_eur = convert_currency(trip_budget, exchange_rate)
    time_needed = calculate_savings_needed(trip_cost_in_eur, savings, monthly_savings)
    travel_month = get_travel_month(time_needed)

    print("\n--- Travel Savings Summary ---")
    print(f"Destination: {destination}")
    print(f"Total Trip Cost in {local_currency}: {trip_budget:,.2f}")
    print(f"Total Trip Cost in EUR: {trip_cost_in_eur:,.2f}")
    print(f"Current Savings: €{savings:,.2f}")
    print(f"Time needed to save: {time_needed} months")
    print(f"Estimated travel-ready date: {travel_month}")

    if time_needed > 0:
        print("Tip: Increase monthly savings to reach your goal sooner!")
        suggest_faster_savings(time_needed, monthly_savings)

    suggest_packing_list(destination, travel_month)

except ValueError:
    print("Error: Please enter valid numerical values.")
