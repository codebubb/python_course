def average_length(list_of_words):
    total = 0
    for word in list_of_words:
        total += len(remove_punctuation(word))
    return total / len(list_of_words)

def remove_punctuation(str):
    # Remove any . , -
    return str

print average_length(["The", "quick", "brown", "fox"])

print average_length(["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"])
