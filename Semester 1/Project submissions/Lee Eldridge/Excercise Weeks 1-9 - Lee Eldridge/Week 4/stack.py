
shopping_list = ["Bananas", "Pears", "Apples"]


print "Welcome to your Shopping list!"
print ""
def p():
    a = raw_input("Would you like to add, view or delete from your shopping list? ").lower()
    if a == "add":
        add = raw_input("What would you like to add to the shopping list? ").title()
        shopping_list.append(add)
        print ""
        print add, "all added!"
        print ""
        p()
    elif a == "view":
        print ""
        for values in shopping_list:
            print values
        print ""
        p()
    elif a == "delete":
        if len(shopping_list) > 0:
            shopping_list.pop()
            print ""
            print "Latest addition to shopping list deleted."
            print ""
        else:
            print ""
            print "No more items on the shopping list left to delete!"
            print ""
        p()
    else:
        print ""
        print "Please enter either add, view or delete."
        print ""
        p()
p()
