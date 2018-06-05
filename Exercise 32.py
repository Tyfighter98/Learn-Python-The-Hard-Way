the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# runs until there are no more elements in the_count
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

# runs from 0-5. Does not include 6!
# "i" automatically increments each run
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # addes the number "i" to the elements list
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")