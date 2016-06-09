print ""
print "Average length of your sentance"
print ""
print "(Type 'Return' to proceed to the next test.)"
print "--------"

def av_len():
    print ""
    user_list1 = raw_input("Type a sentance to find out the average length: ")
    print ""
    if user_list1 == "":
        print "Proceeding..."
    else:
        split_list = user_list1.split()

        total = 0
        average = 0

        for word in user_list1:
            total += len(word)

        average = total / len(split_list)

        print "The average length of your sentance is", average
        av_len()
av_len()
