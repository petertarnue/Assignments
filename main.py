# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


print('')


def read_file_content(filename):
    # [assignment] Add your code here
    
    # open the file in read mode with the context manager
    with open(filename + '.txt', 'r') as file:
        
        # read the file with the read method
        read_file = file.read()
    
    # return the read file +
    return read_file



def count_words(filename):
    # text = read_file_content("./story.txt")
    # [assignment] Add your code here

    # empty dictionary to hold on to the count words
    words_dictionary = {}

    # Read text file
    text = read_file_content(filename)

    # split text into list of words
    text_words = str.split(text, ' ')

    # loop through the list words from the text file
    for word in text_words:

        # check if a word exist in the empty dictionary created above
        if word in words_dictionary:

            # if a word exist in the word dictionary increment/count it by 1
            words_dictionary[word] += 1

        else:
            # if a word doesn't exist in the dictionary equate it to 1
            words_dictionary[word] = 1

    # return the dictionary that contain the words and its count
    return words_dictionary


print(read_file_content('story'))

print('')

print(count_words('story'))
