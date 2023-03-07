import requests

# Function to convert currency using API
def currency_converter(amount, from_currency, to_currency):
    # API endpoint with access key
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    # Making request to the API
    response = requests.get(url)
    # Parsing the JSON response
    data = response.json()
    # Extracting exchange rate for the required currency
    exchange_rate = data["rates"][to_currency]
    # Converting the amount to the required currency
    converted_amount = amount * exchange_rate
    # Returning the converted amount
    return converted_amount

# Testing the function with sample values
amount = 100
from_currency = "USD"
to_currency = "INR"
converted_amount = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
