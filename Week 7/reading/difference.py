'''
difference.py
-------------
Calculate the % difference between two string
'''
import difflib
string1 ='''
This is some text,
it should look similar to string2
'''
string2 ='''
This is some more text,
it should look very similar to string1
'''

s = difflib.SequenceMatcher(None, string1, string2)

print "%.2f" % (s.ratio() * 100), "%"
