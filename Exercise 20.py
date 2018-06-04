from sys import argv

script, input_file = argv

# In the case of this file, f is the file passed into the the argv
def print_all(f):
    print(f.read())

# seek(0) will bring us back to the start of the file
def rewind(f):
    f.seek(0)

# readline() will print the current line until it reaches a '\n' character
# end statement prevents double new line characters
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = '')

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

# Moves to second line of file
current_line += 1
print_a_line(current_line, current_file)

# Moves to third line of file
current_line += 1
print_a_line(current_line, current_file)