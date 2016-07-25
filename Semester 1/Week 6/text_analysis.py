def position_in_alphabet(char):
    letters = "abcdefghijklmnopqrstuvwxyz" # or string.ascii_lowercase
    return letters.index(char.lower()) + 1

def average_length(list_of_words):
    total = 0
    for word in list_of_words:
        total += len(word)
    return total / len(list_of_words)

def last_word(str):
    return str.split()[-1]
