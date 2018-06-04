from sys import argv

script, filename = argv
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that. hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

# truncate() will wipe the file
# By opening the file as read-only the turncate call is redundant since the file is wipped when we
# write the data
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to write these to the file.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# We can add on a new line to each of the write statements just like we could add two strings together
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()

# Since we opened the file as write-only before we must re-open the file as read-only to call read()
target = open(filename, "r")

# To save space we can append read() with a + onto the previous print statement
print("Now here is the contents of the file you just wrote:\n" + target.read())

target.close()