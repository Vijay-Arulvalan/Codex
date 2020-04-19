filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = '' #to hold the digits of pi.
for line in lines:
    pi_string += line.rstrip() #the rstrip() removes all the new line character from each line.
#    pi_string += line.strip()
#the pi_string has a whitespace that is on the left side ... we can get rid of that by using strip() instead of rstrip()


print(pi_string)
#print(pi_string[:32] + '....') #if we want to print first 32 digits from the file.
print(len(pi_string))
