import time
def p():
    file = raw_input("Which file would you like to open? (Please include ext.) ")

    print "Opening", file ,"please wait..."
    time.sleep(3)

    while True:
        try:
            with open(file, 'r') as f:
                read = f.read()
                f.close()
            print "Sorting results..."

            time.sleep(3)
            list = read.split()
            list = [int(x) for x in list]
            list.sort()
            count = 0
            print ""
            for e in list:
                count = count + 1
                print e
            print ""
            print "Here are your list of sorted results! I found", count, "numbers!"
            print ""
            p()
        except IOError:
            print "That file does not exist. Please enter another file name."
            p()
        except ValueError:
            print "That file can not be sorted. Please enter another file name."
            p()


p()
