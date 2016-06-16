key = 'abcdefghijklmnopqrstuvwxyz'

def alpha():
    word = raw_input('Enter a letter to find its numerical value: ')
    if word not in key:
        word = raw_input('You did not enter a letter.\nEnter a letter to find its numerical value: ')
        for i in word:
            n = 1
            x = (key.index(i) + n)
            print x


alpha()
