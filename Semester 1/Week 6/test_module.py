import text_analysis

str = "The quick brown fox jumped over the lazy dog"

print "The string has a an average word length of", text_analysis.average_length(str.split())
print "The last word is ", text_analysis.last_word(str)
print "The position in the alphabet of the first letter of the last word is", text_analysis.position_in_alphabet(text_analysis.last_word(str)[0])
