bus_fare = 2.30

passenger = int(raw_input('Please enter passengers age '))
if passenger <=17:
    print ('Bus fare is '),bus_fare /2
elif passenger >=65:
    print ('Bus fare is free')
else:
    print ('Bus fare is '),bus_fare
