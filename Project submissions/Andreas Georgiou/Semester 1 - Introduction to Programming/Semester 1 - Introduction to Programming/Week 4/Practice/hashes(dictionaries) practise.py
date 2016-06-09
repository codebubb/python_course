# Hashes = Dictionaries in Python

# There are a list of values (the meanings in a dictionary)..
# key (the actual word in a dictionary)

dics = {
        "snake" : "long reptile with no legs",
        "dog" : "mans best friend",
        "cat" : "chases a mouse"
        }



print dics

print dics["snake"] #prints the value of the "snake" key in the dics dictionary.

print dics.keys() #prints a list of keys in a dictionary.


for w in dics:
    print w


for k, v in dics.iteritems():
    #.iteritems() function frints key and value in a dictionary.
    print k, " - Definition: ", v

    print "--------------------------------------------------"

dics1 = {
        "snake" : "long reptile with no legs",
        "dog" : "mans best friend",
        "cat" : "chases a mouse"
        }

dics1.update({"whale" : "very big"})

print dics1
