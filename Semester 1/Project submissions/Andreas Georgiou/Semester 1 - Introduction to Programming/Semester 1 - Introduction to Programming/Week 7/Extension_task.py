
import urllib2

def file_reader():

    open_file = urllib2.urlopen("http://wordpress.org/plugins/about/readme.txt", "r")
    sample = open_file.read()
    open_file.close()
    print "Text to analyse:", "\n", sample

    word_count = 0
    sample_split = sample.split()
    for word in sample_split:
        word_count += 1
    print "\n", "Word count:", word_count

    distinct_word_count = 0
    sample_split_set = set(sample_split)
    for dis_word in sample_split_set:
        distinct_word_count += 1
    print "Distinct word count:", distinct_word_count

    char_count = 0
    char_inc_spac = 0
    for char in sample:
        char_inc_spac +=1
        if char == " ":
            continue
        else:
            char_count += 1
    print "Character count (excl. spaces):", char_count
    print "Character count (inc. spaces):", char_inc_spac

file_reader()

