import time

def greeting():
    time_stamp = time.strftime("%H:%M:%S %d/%m/%y")
    print time_stamp
    if time.strftime("%H%M%S") < "120000" and time.strftime("%H%M%S") > "000000":
        print "Good morning"
    elif time.strftime("%H%M%S") >= "120000" and time.strftime("%H%M%S") <= "180000":
        print "Good afternoon"
    elif time.strftime("%H%M%S") > "180000" and time.strftime("%H%M%S") <= "200000":
        print "Good evening"
    else:
        print "Good night"

greeting()
