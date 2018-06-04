from sys import argv
# exists is used to see if a file exists and returns either true or false
from os.path import exists

script, from_file, to_file = argv

# by appending read() to open there is no need to close the file
indata = open(from_file).read()

# len() returns how many bytes are in a file
print(f"Copyign {len(indata)} bytes from {from_file} to {to_file}")

# exists() will return true if to_file exists or false if it does not
print(f"Does the output file exist? {exists(to_file)}")

# We can use semicolons to put two lines of code on the same line
out_file = open(to_file, 'w') ; out_file.write(indata)

print("Alright, all done.")

out_file.close()