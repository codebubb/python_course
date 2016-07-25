print ""
print "Customer Contact Numbers"
print ""

name_number = {
                    "ronnie sullivan":"01234 567890", "marilyn tucker":"01987 654321",
                    "brad bennett":"01897 65320", "rodney white":"020 765 6655",
                    "brian burton":"01382 763999", "fred fred" : "12345678910",
                    "andy georgiou" : "07939511240"
                    }

def record():
    print ""
    print "--------------------------------------------------------------------"
    print "Customers:"
    print name_number.keys() 
    print""

    print "----------"
    print "(Press 'RETURN' to exit the program.)"
    print "Type 'ADD' to add a new contact or 'PRINT' to print all customer names."
    print ""
    task = raw_input("Enter the name of the customer you wish to contact: ").lower()
    if task == "add":
        add_name = raw_input("Enter new customers name: ")
        add_number = raw_input("Enter new customers contact number: ")
        name_number[add_name] = add_number # adds a new key and value to name_number dictionary.
        record()
    elif task == "print":
        print name_number.keys() # prints the dictionary keys.
        record()
    elif task in name_number:
        print "Customer contact number: ", name_number[task]
        record()
    elif task == "":
        print "Exiting..."
    else:
        print task, " does not exist."
        record()
           
record()
