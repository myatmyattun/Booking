cus_name = input("Enter your name :")
allowed_cities = ["0. New York", "1. Los Angeles", "2. Chicago"]

# Iterate through the list correctly
print("Available allowed_cities:")
for cities in allowed_cities:
    print(cities)

global cities_choice 
cities_choice = int(input("Enter the cities numbers(type just the number): "))   
print("Available allowed_cities:")
for cities in allowed_cities:
    print(cities)


# Get the user's allowed_cities input
global allowed_cities_choice 
allowed_cities_choice = int (input("Which township did you buy the ticket from: "))


def check_cities_choice():
    allowed_places = ["NY", "LA", "Chi"]
    
    # Prompt user for city choice
    cities_choice = int(input("Enter the city number (0 for NY, 1 for LA, 2 for Chi): "))
    
    if cities_choice < 0 or cities_choice >= len(allowed_places):
        return 'Invalid location'
    else:
        # Ask for the city name
        cities_name = input("Enter your city name: ")
        
        # Return valid result
        return f'{cities_name} is valid for {allowed_places[cities_choice]}.'

# Get the result from the function
result = check_cities_choice()

# Print the result
print(result)
  