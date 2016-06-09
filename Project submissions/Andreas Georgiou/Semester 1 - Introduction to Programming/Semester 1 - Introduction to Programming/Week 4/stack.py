print " "
print "A Stack of Fruit"
print " "

fruit_stack = ["Apples" , "Pears" , "Bananas"]
for fruit in range(len(fruit_stack)-1, -1, -1):
        print fruit_stack[fruit]

def fruits():

    print "----------------------------------------------------"
    print "(Press RETURN to exit the program.)"
    print "Type 'PRINT' to print the stack of fruits."
    print "Type 'ADD' to add a fruit to the stack."
    print "Type 'REMOVE' to remove a fruit from the stack."
    user_choice = raw_input("Enter your command: ")
    user_choice = user_choice.lower()

    if user_choice == "":
        print "Exiting..."
    elif user_choice == "add":
        print ""
        add_fruit = raw_input("Enter the fruit you would like to add: ").title()
        print ""
        fruit_stack.append(add_fruit)
        for fruit in range(len(fruit_stack)-1, -1, -1):
                print fruit_stack[fruit]
        print " "
        fruits()
    elif user_choice == "remove":
        print ""
        if len(fruit_stack) == 0:
                print "There is no more fruits in the stack. Try adding some fruits."
                print " "
                fruits()
        else:    
                fruit_stack.pop()
                print ""
                for fruit in range(len(fruit_stack)-1, -1, -1):
                        print fruit_stack[fruit]
                print " "
                fruits()
    elif user_choice == "print":
        print " "
        for fruit in range(len(fruit_stack)-1, -1, -1):
                print fruit_stack[fruit]
        print " "
        fruits()
    else:
        print "Enter a correct command."
        fruits()
        
fruits()
