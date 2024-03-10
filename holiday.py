# Dictionary to store flight costs based on cities
flight_costs = {
    'New York': 300,
    'Paris': 500,
    'Tokyo': 700
}

# Default prices for hotel and car rental
price_per_night = 100
daily_rental_cost = 50

# Functions to calculate costs
def hotel_cost(num_nights):
    return num_nights * price_per_night

def plane_cost(city_flight):
    return flight_costs.get(city_flight, 0)

def car_rental(rental_days):
    return rental_days * daily_rental_cost

def holiday_cost(city_flight, num_nights, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# User inputs
city_flight = input("Enter the city you will be flying to (New York, Paris, Tokyo): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Calculate the total holiday cost
total_holiday_cost = holiday_cost(city_flight, num_nights, rental_days)

# Display holiday details
print("\nHoliday Details:")
print(f"City Flight: {city_flight}")
print(f"Number of Nights at Hotel: {num_nights}")
print(f"Number of Days for Car Rental: {rental_days}")
print(f"Total Holiday Cost: ${total_holiday_cost}")
