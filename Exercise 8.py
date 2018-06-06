# Varibale sets up 4 spaces to be filled by whatever is supplied in the fromat function call
formatter = "{} {} {} {}"

# Calls format function on formatter and fills in the spaces with 1, 2, 3, 4
# As far as I can tell, anything can be supplied into the empty brackets
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))