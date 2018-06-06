# We include the end space not only to add a space after the question, but also to prevent a new line from being added
print("How old are you?", end = ' ')
# input() pronts an input from the user and stores it in the preceeding variable
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("Lets add two numbers: ", end = ' ')
# If we want numbers we can manipulate we need to cast int for the input call
num1 = int(input())
num2 = int(input())
print(f"{num1} + {num2} = ", num1 + num2)