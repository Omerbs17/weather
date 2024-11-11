

import requests

# Function to get weather data for a specific city
def get_weather(city):
    # URL of wttr.in with the city name
    url = f'http://wttr.in/{city}?format=%C+%t+%w+%h'

    # Sending the request to the API
    response = requests.get(url)

    # If the response was successful (status code 200)
    if response.status_code == 200:
        # Print the data received
        print(f"Weather in {city}: {response.text}")
    else:
        print(f"Failed to retrieve data for {city}. Status code: {response.status_code}")

# Get the city name from the user
city = input("Enter the city name: ")

# Call the function to get the weather
get_weather(city)








