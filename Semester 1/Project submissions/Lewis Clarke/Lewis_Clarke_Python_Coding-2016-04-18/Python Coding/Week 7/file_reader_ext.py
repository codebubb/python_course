import urllib

f = urllib.urlopen("https://wordpress.org/plugins/about/readme.txt")
a = f.readlines()
b = ''.join(a)
print ('The number of words in this file is'), b
numbers = sum(c.isdigit() for c in b)
chars   = sum(c.isalpha() for c in b)
print ('In this document there are'),  numbers, ('numbers')
print ('In this document there are'), chars, ('Characters')

count = {}
unique = []
for w in b:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word, times in count.items():
    if times == 1:
        unique.append(word)
print ('In this document there are'), len(unique),('Unique Words')
