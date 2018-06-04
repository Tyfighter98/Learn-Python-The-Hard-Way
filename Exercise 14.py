from sys import argv

# By using quotes in the arguments you can have a single argument include spaces without trailing into
# the next argument
script, user_name, company = argv
prompt = '>>> '

print(f"Hi {user_name} from {company}, I'm the {script}.")
print("I'd liek ot ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")