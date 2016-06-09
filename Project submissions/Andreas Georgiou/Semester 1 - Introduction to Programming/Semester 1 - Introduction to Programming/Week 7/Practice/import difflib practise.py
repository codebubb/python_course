import difflib

string1 =''' This is some text, it should look similar to string2 '''

string2 =''' This is some more text, it should look very similar to string1 '''

s = difflib.SequenceMatcher(None, string1, string2)

print "%.2f" % (s.ratio() * 100), "%"


#By using the difflib.SequenceMatcher class, the strings held in variables string1
#and string2 can be compared and the ratio function provides the percentage of difference.
#The result of the function with the above strings is 89.93%.
