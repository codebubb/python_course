print "Welcome to Customer Relationship Management, Please select a name? Ronnie Sullivan, Marilyn Tucker, Brad Bennett, Rodney White, Brian Burton"
print ""
print "*************************"
customer = {"Ronnie Sullivan" : "01234 567890",
            "Marilyn Tucker" : "01987 654321",
            "Brad Bennett" : "01897 65320",
            "Rodney White" : "020 765 6655",
            "Brian Burton": "01382 763999"
            }
def v():
    c = raw_input("Whose Information Would you like to see? ").title()
    if c in customer: 
        print customer[c]
    else:
        print "Please Check the Name"
    v()
v()
        
    



