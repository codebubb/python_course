from datetime import datetime
now = datetime.now()

if now.hour > 0 and now.hour < 12:
    print "Good Morning,"
elif now.hour >= 12 and now.hour < 18:
    print "Good Afternoon,"
elif now.hour >= 18 and now.hour < 21:
    print "Good Evening,"
elif now.hour >= 21 and now.hour < 24:
    print "Good Night,"

weekday = now.weekday()
if weekday == 1:
    weekday = "Monday"
elif weekday == 2:
    weekday = "Tuesday"
elif weekday == 3:
    weekday = "Wednesday"
elif weekday == 4:
    weekday = "Thursday"
elif weekday == 5:
    weekday = "Friday"
elif weekday == 6:
    weekday = "Saturday"
elif weekday == 7:
    weekday = "Sunday"




print "It is currently %s:%s on" % (now.hour, now.minute), weekday, "the %s/%s/%s." % (now.day, now.month, now.year)

