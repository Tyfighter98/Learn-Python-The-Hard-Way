# We can include the question in the argument of the input function to shorten things
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# By putting input in the arguments of print, input() will be called before printing the prompt
print("How old are you?", input())