with open('pi_digits.txt') as file_object: #whatever we need to do with a file the first thing we need to do is to open the file
#the open function need one argument : the file name.
#“Python looks for pi_digits.txt in the directory where file_reader.py is stored.”
    contents = file_object.read()
    print(contents.rstrip()) #if we want to remove extra line in the end we can use rstrip()
#“The blank line appears because read() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line.”

##to open a file in different path we can use the / to set the file path where the pi_digits is saved:
#with open('Documents/CodeX/Python/pi_digit.txt') as file_object:
