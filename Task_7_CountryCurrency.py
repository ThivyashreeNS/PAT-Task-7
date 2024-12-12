"""Task_7_CountryCurrency.py"""

# Importing the requests module to make HTTP requestsimport requests
import requests

# Class to handle country-related data fetching and processing
class CountryInfo:

    # Constructor to initialize the URL and an empty list for storing country data
    def __init__(self, url):
        self.url = url
        self.countries_data = []


    # Fetch JSON data from the URL
    def fetch_data(self):
        # Make a GET request to the URL
        response = requests.get(self.url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response as JSON and store it
            self.countries_data = response.json()
        else:
            print("Failed to retrieve data.")


    # Method to display the name of countries, their currency names, and symbols
    def display_country_currency_info(self):
        for country in self.countries_data:
            # Get country name
            country_name = country.get('name', {}).get('common', 'Unknown')
            # Get currency information like name and symbol
            currencies = country.get('currencies', {})
            if currencies:
                for currency, details in currencies.items():
                    currency_name = details.get('name', 'Unknown')
                    currency_symbol = details.get('symbol', 'N/A')
                    # Print country name, currency name, and symbol
                    print(f"Country: {country_name}, Currency: {currency_name}, Symbol: {currency_symbol}")
            # If no currency info is available
            else:
                print(f"Country: {country_name}, Currency: No currency info available.")


    # Method to display countries that use Dollar as their currency
    def display_countries_with_dollar(self):
        # List to store countries using Dollar
        dollar_countries = []
        for country in self.countries_data:
            country_name = country.get('name', {}).get('common', 'Unknown')
            currencies = country.get('currencies', {})
            # Check if USD is the currency code add country to the list
            if 'USD' in currencies:
                dollar_countries.append(country_name)
        print("Countries using Dollar (USD) as currency:")
        for country in dollar_countries:
            print(country)


    # Method to display countries that use EUR (Euro) as their currency
    def display_countries_with_euro(self):
        # List to store countries using Euro
        euro_countries = []
        for country in self.countries_data:
            country_name = country.get('name', {}).get('common', 'Unknown')
            currencies = country.get('currencies', {})
            # Check if EUR is the currency code and add country to the list
            if 'EUR' in currencies:
                euro_countries.append(country_name)
        print("Countries using Euro (EUR) as currency:")
        for country in euro_countries:
            print(country)


# URL containing all country information
url = "https://restcountries.com/v3.1/all"

# Creating an object of the CountryInfo class
obj = CountryInfo(url)

# Fetching data
obj.fetch_data()

# Displaying country name, currency, and currency symbols
obj.display_country_currency_info()

# Displaying countries with Dollar as currency
obj.display_countries_with_dollar()

# Displaying countries with Euro as currency
obj.display_countries_with_euro()
