#Relative path
#its longer but it will clarify python where it want to look.

file_path = '/Users/vijay/Documents/Codex/Python/pi_digit.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)
