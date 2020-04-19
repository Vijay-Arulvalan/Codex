#Word_count

def count_words(filename):
    """Count the approximate word in the file"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        print('The file you search to count is not there')

    else:
        """Count the approximate words in file"""
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + ' has ' + str(num_words) + ' words.')

filename = 'alice.txt'
count_words(filename)
