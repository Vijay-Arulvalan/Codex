#Word_count with loop for multiple files

def count_words(filename):
    """Count the approximate word in the file"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
#        pass #if we use pass then this error wont be considered it will pass silently
        print('The file you search to count is not there')

    else:
        """Count the approximate words in file"""
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + ' has ' + str(num_words) + ' words.')

# to loop the count of multiple files
filenames = ['alice.txt', 'sidhartha.txt', 'little_women.txt', 'moby_dick.txt']
for filename in filenames:
    count_words(filename)
