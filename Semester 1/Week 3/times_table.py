'''
times_table.py
--------------
Ask user for input and then display a times table
'''

user_number = raw_input("Which times table do you want to display?")

# If the user has not entered a valid number
if not user_number.isdigit():
    print user_number, "is not a number\nPlease try again."
else:
    # Convert the user input string into an integer
    user_number = int(user_number)

    for i in range(1,11):
        print i, "\tx\t", user_number, "\t=\t", i * user_number


        
