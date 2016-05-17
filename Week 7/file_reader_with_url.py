# Stats on words in a file
import urllib

def word_count(txt):
    return len(word_data.split(' '))

def unique_words(txt):
    return len(set(word_data.split(' ')))

def total_chars(txt):
    return len(word_data)


url = urllib.urlopen('https://wordpress.org/plugins/about/readme.txt')
word_data = url.read()

print "Total words: \t", word_count(word_data)
print "Unique words:\t", unique_words(word_data)
print "Total chars:\t", total_chars(word_data)
