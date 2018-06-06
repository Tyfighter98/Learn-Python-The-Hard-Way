# The backslash allows us to include characters that are ususally interpreted by python as some kind of operator
# \t creates a tab in
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# \r will remove everything that preceded it on the line
# \b allows us to delete teh preceding character
# \v moves the text following vertically down a line while still in line horizontally
test_cat = """
This is a\rCarriage retu\brn
And\vthis\vis\va\vvertical\vtab
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)
print(test_cat)