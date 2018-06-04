program_name = "Python"

print("Fill in the blank:")

# By using the empty braces we can insert data later with .format
name = "My name is {} and I am {} years old."

# Use .format to insert data into the empty braces of a variable
# By using a comma we can also chain together to formating methods in a single print statement
print(f"This is the into to {program_name}.", name.format("Tyler Warren", 20))
