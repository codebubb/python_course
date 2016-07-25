import time;
import calendar
def get_time():
    my_time = time.strftime("%H:%M:%S")
    my_time = time.strftime("%H:%M:%S")
    if time.strftime("%H") > 12 >= 0:
        print 'Good Morning The time is:', my_time
    elif time.strftime("%H") < 12 <= 18:
        print 'Good afternoon The time is:', my_time
    else:
        print 'Good Evening The time is:', my_time

print time.strftime("%d:%m:%y")
get_time()
