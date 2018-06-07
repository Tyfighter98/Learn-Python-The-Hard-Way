ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let me fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Bannana", "Girl", "Boy"]

while len(stuff) != 10:
    # removes the last item in more_stuff and places it into next_one
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print(f"There we go: {stuff}")

print("Let\'s do some things with stuff.")

print(stuff[1])
# selects the last item and prints it
print(stuff[-1])
# selects and removes the last item in the list
print(stuff.pop())
print(' '.join(stuff))
# joins the item in index 3 with index 5 and uses '#' as the glue
print('#'.join(stuff[3:5]))