'''
bus_price.py
------------
Calculate the correct fare for bus travellers
'''

age = int(raw_input("What is the passenger's age?"))
if age > 65:
    price = 0
elif age <18:
    price = 1.15
else:
    price = 2.305

print "Your bus fare is \xa3   %.2f  " % price # %.2f is the formatting for a float
                                            # to 2 decimal places
