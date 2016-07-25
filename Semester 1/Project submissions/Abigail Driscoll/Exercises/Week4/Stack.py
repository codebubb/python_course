stack = ["English Language", "Maths", "Physics"]
# classes.pop(0)
# print(classes)
# classes.append("Government and Politics")
# classes.append("ICT")
# print(classes)
# classes.pop()
# print(classes)

decision = input("Would you like to 1. ADD items to the stack. 2. DELETE items from the stack 3. VIEW the current stack:  ")
if decision == '1':
    addnew = input("What item would you like to add to the classes stack? ")
    stack.append(addnew)
    print(stack)
elif decision == '2':
    delete = int(input("What item would you like to delete from the classes stack? (Please state index number) "))
    stack.pop(delete)
    print(stack)
elif decision == '3':
    print(stack)
else:
    print("Sorry, you must enter 1, 2 or 3'.")
