filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() #the readlines() take each line from the file and store it in list.
    for line in lines:
        print(line.rstrip()) #rstrip() is used to delete the invisible new line character in the file
#“These blank lines appear because an invisible newline character is at the end of each line in the text file.
#The print statement adds its own newline each time we call it”
