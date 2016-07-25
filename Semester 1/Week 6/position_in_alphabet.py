def position_in_alphabet(char):
    letters = "abcdefghijklmnopqrstuvwxyz" # or string.ascii_lowercase
    return letters.index(char.lower()) + 1

print "A =", position_in_alphabet("A")
print "P =", position_in_alphabet("P")
print "Z =", position_in_alphabet("Z")
