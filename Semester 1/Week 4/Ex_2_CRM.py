customers = {   "Ronnie Sullivan"   : "01234 567890",
                "Marilyn Tucker"    : "01987 654321",
                "Brad Bennett"      : "01897 65320",
                "Rodney White"      : "020 765 6655",
                "Brian Burton"	    : "01382 763999" }

while True:
    search = raw_input("Which customer's number do you need? (Enter EXIT to finish)")
    if search == "EXIT":
        break;
    if search in customers.keys():
        print "Call ", search, "on ", customers[search]
    else:
        print "Couldn't find a number for ", search


