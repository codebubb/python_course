from  collections import Counter

f = """So far we've  encountered two ways of writing values
expression statements and the print statement. (A third way
is using thewri te()  method of file objects; the standard output
file can be referenced as sys.stdout. See the Library Reference for
more information on this.)Often you'll want more control over the
formatting of your output than simply printing space-separated values.
There are two ways  to format your output; the first way is  to do all
the string handling yourself; using string slicing and concatenation
operations you can create any layout you can imagine. The string types
have some methods that perform useful operations for padding strings to
a given column width; these will be discussed shortly. The second way is
to use  the str.format()  method.The string module contains a Template
class which offers yet another way to substitute values into strings.One
question remains, of course: how do you convert values to strings? Luckily,
Python has ways  to convert any value to a string: pass  it to the repr()
or str()  functions.The str()  function is meant to return representations
of values which are fairly human-readable, while repr() is meant to generate
 representations which can be read by the interpreter (or will force a
 SyntaxError if there is no equivalent syntax).For objects which don't have
 a particular representation for human consumption, str() will return the same
 value as repr(). M any values, such as  numbers or structures  like lists
 and dictionaries, have the same representation using either function. Strings
 and floating point numbers, in particular, have two distinct representations"""

print ('The number of words in this file are'), len(f.split())
numbers = sum(c.isdigit() for c in f)
chars   = sum(c.isalpha() for c in f)
print ('In this document there are'),  numbers, ('numbers')
print ('In this document there are'), chars, ('Characters')

count = {}
unique = []
for w in f.split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word, times in count.items():
    if times == 1:
        unique.append(word)
print ('In this document there is'), len(unique),('Unique Words')
