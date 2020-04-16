prompt = "\n Tell  me something and I'll  repeat after you."
prompt += "\n Enter 'quit' to end the program: "

active = True       # The program starting with active state we gave True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
