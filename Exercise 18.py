# def defines a function and must end the line with a semi-colon
# functions are just like variable names. They must start with a letter
# The '*' tells Python to take all the arguments from the function and put them into args as a list
def print_two(*args):
        arg1, arg2 = args
        print(f"arg1: {arg1}, arg2: {arg2}")

# while print_two works, it is much more efficent and space saving to just put the variable names inside the arguments of the function
def print_two_again(arg1, arg2):
        print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
        print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("Tyler", "Warren")
print_two_again("Tyler", "Warren")
print_one("First!")
print_none()