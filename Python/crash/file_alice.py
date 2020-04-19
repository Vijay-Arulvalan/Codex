filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    msg = "The file you searching is not found"
    print(msg)

else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has " + str(num_words) + ' words')
    print(words)
