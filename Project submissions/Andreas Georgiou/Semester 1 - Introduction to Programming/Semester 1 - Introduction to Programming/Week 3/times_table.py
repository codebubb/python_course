print ""
print "Times Tables \n"

    
def timestables():
    table = raw_input("Which times table do you want to see? ")
    if table.isdigit() == False:
        print "You must enter numbers only."
        timestables()
    else:
        table = int(table)
    up_to = raw_input("What would you like your times table to go up to? ")
    if up_to.isdigit() == False:
        print "You must enter numbers only."
        timestables()
    else:
        up_to = int(up_to)

    for i in range(1,up_to +1):
        print ""
        print i, " x ", table, " = ", i * table
        print ". . . . . . . . ."
    print "-----------------------------------------------------"
    timestables()
        
timestables()
