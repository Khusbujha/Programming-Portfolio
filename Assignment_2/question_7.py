"""This program takes a list of city names and displays:
The total number of cities entered,
The number of cities that start with the letter 'K',
The list of all cities in alphabetical order
"""

city = input("Enter the names of cities seperated by comma :").split(",")
city = [c.upper().strip() for c in city]
print("The number of cities is:", len(city))
print(city)
k_city = [c for c in city if c.startswith("K")]
print("The number of cities that starts with 'K' is:", len(k_city))
print(k_city)
print("The sorted list of cities:")
print(sorted(city))
