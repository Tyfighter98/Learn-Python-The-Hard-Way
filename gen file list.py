from os import walk
from sys import argv

script, path = argv

files = open("file list.txt", 'w')

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

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

for i in f:
    if "Exercise" in i:
        files.write(i + get_num(i))
        print(i)
    else:
        continue

f.sort()
print("\n\n\n")

for i in f:
    if ".py" and "Exercise" in i:
        print(i)
    else:
        continue

def get_num(file_name):
    sub = file_name.split(" ")
    return int(sub[1])