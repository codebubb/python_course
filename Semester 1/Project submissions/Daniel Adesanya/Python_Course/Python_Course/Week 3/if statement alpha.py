def p():
    
    user_type = raw_input("Is Lee a ladies man? ").lower()
    if user_type == "yes":
        print "Lee like BBW"
    elif user_type == "No":
        print "Lee likes Lindsey very much"
    elif user_type != "no" or "yes":
        print "Baby got back"
    p()
p()
    
