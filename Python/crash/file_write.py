filename = 'programming.txt'

with open(filename, 'W') as file_object:
#“You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+').
#If you omit the mode argument, Python opens the file in read-only mode by default.”
    file_object.write("I love programming learning.") #\n if we use then the next line print to the next line or else it will print in string
    file_object.write("I love to learn things.")

# to append:
#with open(filename, 'a') as file_object:
#    file_object.write("I love programming learning.") #\n if we use then the next line print to the next line or else it will print in string
#    file_object.write("I love to learn things.")
