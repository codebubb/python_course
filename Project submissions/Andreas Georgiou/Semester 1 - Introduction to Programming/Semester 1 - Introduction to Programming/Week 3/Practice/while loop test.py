# As an alternative to for loops, which will loop a finite amount of times
# through a list provided, you can use a while loop which will continue to
# repeat code until a certain Boolean condition has been met.
# A while loop will execute the lines of code underneath it whilst the
# condition provided is True.

counter = 10

while counter > 3:
    print "counter on ", counter, " and still going!"
    counter -= 1

print "-" * 20

while raw_input("What number between 1-20 am i thinking of? ") != "8":
    print "Nope! Try again."
