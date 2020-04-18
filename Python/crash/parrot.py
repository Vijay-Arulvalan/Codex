prompt = "\n Tell  me something and I'll  repeat after you."
prompt += "\n Enter 'quit' to end the program: "
message  = ""

while message != 'quit':
    message = input(prompt)
#    print('\n' + message) #if there no if condition then the program repeats if we say quit also
    if message != 'quit': #if message not equal to quit then only print message
        print('\n' + message)
