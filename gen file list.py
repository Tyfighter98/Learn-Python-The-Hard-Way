from os import walk
from sys import argv

# requires an argument of path at run time to determine which directory to scan
script, path = argv

files = open("README.txt", 'a')

files.write("\n\nExercise Breakdown:\n")

chapters = {5 : "More variables and printing", 6 : "Strings and text", 7 : "More printing",
8 : "Printing, printing", 9 : "Printing, printing, printing", 10 : "What was that?",
11 : "Asking questions", 12 : "Prompting people", 13 : "Parameters, Unpacking, Variables",
14 : "Prompting and Passing", 15 : "Reading Files", 16 : "Reading and Writing Files",
17 : "More Files", 18 : "Names, Variables, Code, and Functions", 19 : "Functions and Variables",
20 : "Functions and Files", 21 : "Functions Can Return Something", 22 : "What do you know so far?",
23 : "Strings, Bytes, and Character Encodings", 24 : "More Practice", 25 : "Even More Practice",
26 : "Congradulations, Take a Test!", 27 : "Memorizing Logic", 28 : "Boolean Practice",
29 : "What if", 30 : "Else and if", 31 : "Making Decisions", 32 : "Loops and Lists", 33 : "While Loops",
34 : "Accessing Elements of Lists", 35 : "Branches and Functions", 36 : "Designing and Debugging",
37 : "Symbol Review", 38 : "Doing Things to Lists", 39 : "Dictionaries, Oh Lovely Dictionaries",
40 : "Modules, Classes", 41 : "Learning to Speak Object-Oriented", 42 : "Is-a, Has-a, Objects, and Classes",
43 : "Basic Object-Oriented Analysis and Design", 44 : "Inheritance Verssu Compositon",
45 : "You Make a Game", 46 : "A Project Skeleton", 47 : "Automated Testing", 48 : "Advanced User Input",
49 : "Making Sentences", 50 : "Your First Website", 51 : "Gettign Input from a Browser",
52 : "The Start of Your Web Game"}

def get_num(file_name):
    sub = file_name.split(" ")
    # sub[1] is "<num>.py"
    num = sub[1]
    # num[:-3] removes the last 3 chracters (".py") from the string
    num = num[:-3]
    # cast num as int so we can use it as a key
    return int(num)

f = []
# cycles through all directory paths, directory names, and filenames
for (dirpath, dirnames, filenames) in walk(path):
    # add the filenames to the end of the list f
    f.extend(filenames)
    break

for i in f:
    if "Exercise" in i:
        files.write(i + ": " + chapters[get_num(i)] + "\n")
    else:
        continue