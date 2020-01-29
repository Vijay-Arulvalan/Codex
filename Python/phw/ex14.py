from sys import argv

script, user_name = argv
prompt= '> '

print(f"Hi this is {user_name} and i am {script} script.")
print("I'd like to ask you a few question.")
print(f"Do you like me {user_name}? ")
likes = input(prompt)

print(f"Where do you live {user_name}? ")
lives  = input(prompt)

print("What kind of computer do you have? ")
computer = input(prompt)

print(f"""
        Hi, So you said {likes} about liking me.
        You live in {lives}. Not sure where that is.
        And you have a {computer} computer. that's nice.""")
