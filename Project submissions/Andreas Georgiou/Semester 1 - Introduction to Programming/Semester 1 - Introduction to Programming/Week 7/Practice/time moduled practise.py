# Unix epoch is a set date in time; Thursday, 1 January 1970 (the current date)

# Unix time is the number of seconds that has passed since this date



import time

print time.time() # prints unix time



print time.strftime("%H:%M:%S") # prints formated time

print time.strftime("%d/%m/%y") # prints formated date

print time.strftime("%d/%m/%y , %H:%M:%S")
