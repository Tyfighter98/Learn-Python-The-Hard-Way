def dungeon():
    print("You awake in an empty room unsure of how you got there.")
    print("All you see in the room is a podium with a mysterious book lying open on it.")
    print("What do you do?")

    print("\n1) Close the book")
    print("2) Read the book\n")

    choice = input("> ")

    if choice == "1":
        print("When you close the book you notice a door behind you and you walk through it.")
        entrance()
    elif choice == "2":
        print("\nUpon reading the book you see a bright flash of green light.")
        dream_world()
    else:
        print("\nYou die of being overencumbered.")
        dead()

def dream_world():
    print("You awake surrounded by a sea of green liquid with a squid like figure standing in front of you.")
    print("What do you do?")

    print("\n1) Pull his tenticals")
    print("2) Try to make conversation\n")

    choice = input("> ")

    if choice == "1":
        print("\nHe pushes you into the liquid and you drown.")
        dead()
    elif choice == "2":
        print("\nHe greets you and gives you 25 Shmekles.")
        print("Unfortunatly, you have no way to leave and you die with your loot")
        dead()
    else:
        print("\nYou are dizzied by looking at the swirlling liquid and you walk in and drown.")
        dead()

def entrance():
    print("You may not have gotten any loot, but at least you made it out alive!")
    exit()

def dead():
    print("\nGame Over")
    exit()

dungeon()