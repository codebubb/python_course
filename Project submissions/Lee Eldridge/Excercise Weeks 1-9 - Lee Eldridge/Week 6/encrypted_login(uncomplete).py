import string
alphabet = string.lowercase[:26]
alphabet = [str(i) for i in alphabet]

alphabet_2 = string.lowercase[13:26]+string.lowercase[0:13]
alphabet_2 = [str(i) for i in alphabet_2]


dictionary = dict(zip(alphabet, alphabet_2))

#hello = raw_input("Enter a word: ")

for key,value in dictionary.iteritems():
    print key, "=", value
    

