# Run with "python 'Exercise 15.py' '.\Supplimental Files/ex15_sample.txt"
from sys import argv
script, filename = argv
# Before we can read the file or do anything else we must open it!!
txt = open(filename)

print(f"Here's your file {filename}:")
# .read() will return the contents of the opened file
# Notice that read() had to be inside a print statement in order to be outputed on the terminal
print(txt.read())

# We can put "Supplimental Files/ex15_sample.txt" as is without quotes to read the file from the other folder
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# Tells python we are done with the file. Very important!
txt.close()
txt_again.close()