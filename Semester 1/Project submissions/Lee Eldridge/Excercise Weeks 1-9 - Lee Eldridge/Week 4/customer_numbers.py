customers = {
"Ronnie Sillivan" : "01234567890",
"Marilyn Tucker" : "01987654321",
"Brad Bennett" : "0189765320",
"Rodney White" : "0207656655",
"Brian Burton" : "01382763999"
}
"Ronnie Sillivan" in customers
print "Welcome to the number finder!"

def p():    
    purpose = raw_input("Would you like to: find a number by name (name), name by number (number) or view the full list (view)? ").lower()
    if purpose == "name":
        number_finder = raw_input("Please enter the name for the person you are looking for. ")   
        if number_finder in customers:
            print "%s's number is:" % (number_finder), customers[number_finder]
            print ""
        else:
            print "This name does not exist on our database. Please try another."
            print ""
    elif purpose == "number":
        name_finder = raw_input("Please enter the number for the person you are looking for. ")   
        for name, number in customers.iteritems():
            if number == name_finder: 
                print name, "'s number is %s." % (name_finder) 
                print ""
                break
        else:
            print "This number does not exist on our database. Please try another."
            print ""
    elif purpose == "view":
        for name, number in customers.iteritems():
            print name, ":", number
    elif purpose == "add":
        new_name = raw_input("Please enter the new customers name: ")
        new_number = raw_input("Please enter the new number for the customer: ")
        customers[new_name] = new_number
        print ""
        print "All added, thank you."
        print ""
        p()  
    else:
        "Please enter either: name, number or view."

    p()

p()

