# For dictionaries you enter things just like you would a list
# However in dictionaries you enter "<index> : <data>, ..."
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print(f"NY State has: {cities['NY']}")
print(f"OR State has: {cities['OR']}")

print('-' * 10)
print(f"Michigan's abbreviation is: {states['Michigan']}")
print(f"Florida's abbreviation is: {states['Florida']}")

print('-' * 10)
print(f"Michigan has: {cities[states['Michigan']]}")
print(f"Florida has: {cities[states['Florida']]}")

print('-' * 10)
# Notice we must use list to get the items in states even though states is a dictionary
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated as {abbrev}")

print('-' * 10)
# abbrev stores the "index" of cities and city sotres the data in that "index"
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')
if not state:
    print("Sorry, Texas is not in the dictionary.")

# The second argument of get is a fallback that is returns if there is nothing at the requested index
city = cities.get('TX', 'Does not exists')
print(f"The city for the state 'TX' is: {city}")

armours = {
    'Legs' : 'Grieves',
    'Chest' : 'Breastplate',
    'Head' : 'Helmet',
    'Feet' : 'Boots',
    'Right Hand' : "Sword",
    'Left Hand' : "Shield"
}

print('-' * 10)
# We can also use other features such as sorted() on dictionaries
for body_part, armour in sorted(list(armours.items())):
    print(f"{armour} goes on the {body_part}")

print('-' * 10)
print("Please enter the body part you would like to learn about:")

part = input('> ')

# Safely querry input from the user in your dictionary
info = armours.get(part, part + " is not a valid body part.")
print(f"{part}: {info}")