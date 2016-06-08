def alength():
    string = input("Please enter a list of words: ") + " "
    length = len(string)
    spaces = string.count(" ")
    words = length - spaces
    average = (words)/(spaces)
    print(average)

alength()