def break_words(stuff):
    '''This function will break up words for us.'''
    # Will add new items to the list of words after every ' '
    words = stuff.split(' ')
    return words

def sort_words(words):
    # Sorted is built in and will automatically put the passed in items in alphabetical order
    return sorted(words)

def print_first_word(words):
    # pop will take remove the selected item from a list at the passed in location
    word = words.pop(0)
    print(word)

def print_last_word(words):
    # -1 will select the last item
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)