# run "python Exercise\ 13.py <first> <second> <third> <name>"
# required to use arguments for the script
from sys import argv
#script will return the name of the script being run
# first, second, and third are unpacked from argv as the 3 parameters entered by the user
script, first, second, third, name = argv

print("The script is called:", script)
print("The first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Combines argv parameters with input()
age = input("How old are you? ")
print(f"{name} is {age}.")
# We can cast varaibles from argv as int or anything else to convert it from a string
print("In five years you will be", int(age) + 5)