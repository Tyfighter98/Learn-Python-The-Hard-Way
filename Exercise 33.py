from sys import argv

# You need script in argv!
script, increment = argv

i = 0
runs = 6
numbers = []

while i < runs:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + int(increment)
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)