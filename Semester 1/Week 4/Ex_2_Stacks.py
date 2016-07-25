'''
stacks.py
---------
Simple demonstration of stacks
'''
import os

stack = []
os.system('cls')

while True:
    print '''
Stack menu
----------
1) Display the stack
2) Add to the stack
3) Remove item from the stack
          '''
    option = int(raw_input("Choose an option:"))
    if option == 3 and len(stack)>0:
        os.system('cls')
        print "--- Removed from stack ---"
        print stack.pop()
        print "--------------------------"

    elif option == 2:
        new_value = raw_input("Enter a value to add to the stack:")
        os.system('cls')
        stack.append(new_value)
        print "--- Added to stack ---"
        print new_value
        print "----------------------"
    else:
        os.system('cls')
        if len(stack) > 0 :
            print "\n--- Current Stack ---"
            for i in range(len(stack), 0, -1):
                print "[",i-1, "]", stack[i-1]
            print "--- End of Stack ---"
        else:
            print "\n--- Stack Empty ---"
    print "\n"
