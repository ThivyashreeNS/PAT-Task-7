"""Task_7_BreweryData.py"""

# Importing the requests library to make HTTP requests
import requests


# Class to manage brewery data and operations
class BreweryData:
    def __init__(self, state):
        # Initializes the class with a state name and a URL for the Open Brewery DB API.
        self.state = state
        self.url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
        # Fetch the brewery data for this state
        self.breweries = self.fetch_breweries()


    # Fetches brewery data from the API and returns the list of breweries.
    def fetch_breweries(self):
        # Send GET request to the API
        response = requests.get(self.url)
        # Check if the request was successful and return the JSON data as a list of breweries
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve data for {self.state}.")
            return []


    # Lists the names of all breweries in the state.
    def list_breweries(self):
        print(f"\nBreweries in {self.state}:")
        for brewery in self.breweries:
            # Print each brewery's name
            print(f"- {brewery['name']}")


    # Returns the total number of breweries in the state.
    def count_breweries(self):
        return len(self.breweries)


    # Counts the types of breweries in each city in the state.
    def count_brewery_types_by_city(self):
        # Dictionary to store brewery types by city
        city_brewery_types = {}
        for brewery in self.breweries:
            # Get the city, default to 'Unknown'
            city = brewery.get('city', 'Unknown')
            # Get the brewery type
            brewery_type = brewery.get('brewery_type', 'Unknown')

            # If the city is not in the dictionary, add it
            if city not in city_brewery_types:
                city_brewery_types[city] = {}

            # Count brewery types in the city
            if brewery_type in city_brewery_types[city]:
                # Increment the count for the brewery type
                city_brewery_types[city][brewery_type] += 1
            # Initialize the count for the new brewery type
            else:
                city_brewery_types[city][brewery_type] = 1

        # Print the counts of brewery types for each city
        for city, types in city_brewery_types.items():
            print(f"\nCity: {city}")
            for brewery_type, count in types.items():
                print(f"- {brewery_type}: {count} breweries")



    # Counts how many breweries have websites in the state and lists them.
    def count_breweries_with_websites(self):
        # Filter breweries with websites
        breweries_with_websites = [brewery for brewery in self.breweries if brewery.get('website_url')]
        print(f"\nBreweries in {self.state} with websites:")
        # Print name and website URL
        for brewery in breweries_with_websites:
            print(f"- {brewery['name']} ({brewery['website_url']})")
        # Return the count of breweries with websites
        return len(breweries_with_websites)


# The states we want to process
states = ['Alaska', 'Maine', 'New York']

if __name__ == '__main__':
    for state in states:
        # Create an instance of BreweryData for each state
        obj = BreweryData(state)

        # Task 1: List the names of all breweries in the state
        obj.list_breweries()

        # Task 2: Count and print the total number of breweries in the state
        count = obj.count_breweries()
        print(f"\nTotal number of breweries in {state}: {count}")

        # Task 3: Count and print the number of types of breweries by city
        obj.count_brewery_types_by_city()

        # Task 4: Count and list the breweries with websites
        website_count = obj.count_breweries_with_websites()
        print(f"\nTotal number of breweries with websites in {state}: {website_count}")
        # Separator between states
        print("=" * 40)
