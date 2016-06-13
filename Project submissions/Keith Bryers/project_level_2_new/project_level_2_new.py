# -*- coding: utf-8 -*-

# The above allows the use of £ signs, however, command prompt still will not.

#!/usr/bin/python

''' N.B. Please use in either command prompt or an IDLE which allows the os.system('cls') to clear the screen. Thanks.'''

import os
import sys
import time

time_stamp = time.strftime("%d %b %y, %H:%M:%S")

bank = True
# loop

D = []
# deposit list
W = []
# withdraw list
T = []

user_1 = ["1234", 0]
user_2 = ["5678", 0]
# static variables        

# User ID Entry

def login():
    
    print ""
    print "------------"
    print "LOGIN SYSTEM"
    print "------------"

    try:
        global user_id
        # used a global variable as this will be used all the way throughout the code
        # saves me having to assign the variable each time. Reduces lines.
        user_id = str(raw_input("USER ID : ").lower())
        
        if user_id == "keith":
            
            f = open(user_id + ".txt", "r")
            stored_pin = int(f.readline().strip()) # used the strip to place file contents into variable a string and NOT list. Stored as integer to prevent,
            # concatenation error.
            # taking the user_id from the raw_input and opening a file under the users name
            global stored_balance
            # same as above, however not used throughout.
            stored_balance = int(f.readline().strip())
            for trial in range(3):
                pin = int(raw_input("PIN : "))
                if pin == stored_pin:
                    break
                elif pin != stored_pin:
                    print "Incorrect Pin, Try again"
            else:
                print "Max login attempts reached, exiting to login screen"
                login()
                # didn't find password after 3 attempts

                # above is a login attempt system using range and a for loop.
         
        elif user_id == "jade":
            f = open(user_id + ".txt", "r")
            stored_pin = int(f.readline().strip())
            stored_balance = int(f.readline().strip())
            for trial in range(3):
                pin = int(raw_input("PIN : "))

                if pin == stored_pin:
                    break
            else:
                print "Max login attempts reached, exiting to login screen"
                login()
                # didn't find password after 3 attempts

        # repeat of the above code, but just with a different user

        else:
            if user_id != "jade":
                print "Username does not exist, please try again"
                os.system('cls') # clears the screen. Better for aesthetics :)
                login() # asked it to revert back to login start if the pin is wrong for a final time

            elif user_id != "keith":
                print "Username does not exist, reloading login."
                os.system('cls')
                login()
            # If I used nested dictionaries, I could create a user database containing
            # User names of all users.


    except ValueError:
        print("Str, Please.")
        # NOT sure if needed as hard coded to only accept exact user names, otherwise, it reverts back to beginning.


def deposit():
    try:
        print "-" * 25
        deposit = int(raw_input("Deposit amount: $ ")) # again placing an int() to avoid concatenation error
        
        global d_new_bal # used extensively throughout the program, fitting then to use as global variable
        
        if user_id == "keith":
            with open(user_id + '.txt', 'r') as f:
                data = f.readlines()
                # open file using user_id
                d_new_bal = int(data[1]) + deposit
                # creating new balance based on the deposit amount
                d_d_t = "$ +" + str(deposit) + " : " + time_stamp
                # creating a variable with both the deposit amount and time stamp (date & time)
                T.append(d_d_t)
                # appended this variable into the above deposit list D
                user_1[1] = d_new_bal
                # changed the above static variable. This probably doesn't need to be in here. 
                print ""
                print "Deposit Successful"
                print ""
                print "Your new balance is: $ ", d_new_bal
                print "-" * 25
                # particularly pleased with the below. This could have been done more simply, but I couldn't figure out another way...
                with open(user_id + '.txt', 'r') as f:
                    # open file again using user_id
                        data = f.readlines()
                        # write all the data in the file into list
                        data[1] = str(d_new_bal)
                        # modify the second value in the list (the balance) to reflect new balance.    
                with open(user_id + ".txt", "w") as f:
                        f.writelines(data)
                # write all the data back into the text file including the new updated balance.
                
        if user_id == "jade":
            with open(user_id + '.txt', 'r') as f:
                data = f.readlines()                
                d_new_bal = int(data[1]) + deposit
                d_d_t = "$ " + str(deposit) + " : " + time_stamp
                T.append(d_d_t)
                user_2[1] = d_new_bal
                print ""
                print "Deposit Successful"
                print ""
                print "Your new balance is: $ ", d_new_bal
                print "-" * 25
                with open(user_id + '.txt', 'r') as f:
                        data = f.readlines()
                        data[1] = str(d_new_bal)
                with open(user_id + ".txt", "w") as f:
                        f.writelines(data)
                # same as above, just with a different user
    except ValueError:
        print("Int, please.")
        
        # value error used to prevent characters being used instead of integers.
        
        # the above, keeps a live balance constantly. Which has proven difficult to achieve without the above sequence.
    
def withdraw():
    try:
        print "-" * 25
        withdrawal = int(raw_input("Withdrawal amount: $ "))

        # exat same commenting as deposit with the below exceptions
        global w_new_bal
    
        if user_id == "keith":
            with open(user_id + '.txt', 'r') as f:
                    data = f.readlines()
                    if int(data[1]) - withdrawal < -100:                
                        print "Sorry Insufficient Funds"
                        # incorporated an overdraft on the users account of £100
                        # this also prevents the withdrawal being added to the list when there has been no successful withdrawal.
                    else:
                        with open(user_id + '.txt', 'r') as f:
                            data = f.readlines()
                            w_new_bal = int(data[1]) - withdrawal
                            w_d_t = "$ -" + str(withdrawal) + " : " + time_stamp
                            T.append(w_d_t)
                            user_1[1] = w_new_bal
                            print ""
                            print "Withdrawal Successful"
                            print ""
                            print "Your new balance is: $ ", w_new_bal
                            print "-" * 25

                            with open(user_id + '.txt', 'r') as f:
                                data = f.readlines()
                                data[1] = str(w_new_bal)
        
                            with open(user_id + ".txt", "w") as f:
                                f.writelines(data)
        

    
        if user_id == "jade":
            with open(user_id + '.txt', 'r') as f:
                    data = f.readlines()
                    if int(data[1]) - withdrawal < -100:                
                        print "Sorry Insufficient Funds"
                        
                    else:
                        with open(user_id + '.txt', 'r') as f:
                            data = f.readlines()
                            w_new_bal = int(data[1]) - withdrawal
                            w_d_t = "$ " + str(withdrawal) + " : " + time_stamp
                            T.append(w_d_t)
                            user_1[1] = w_new_bal
                            print ""
                            print "Withdrawal Successful"
                            print ""
                            print "Your new balance is: $ ", w_new_bal
                            print "-" * 25

                            with open(user_id + '.txt', 'r') as f:
                                data = f.readlines()
                                data[1] = str(w_new_bal)
        
                            with open(user_id + ".txt", "w") as f:
                                f.writelines(data)

    except ValueError:
        print("Int, please.")
         

def transactions():
    print "Here is a list of your transactions: "
    for i in T: # printing transaction list
        print str(i)

''' CHANGE MADE : after testing, this was the better option. To merge the lists into 1 transaction list. Similar to bank systems.'''

    # try:
        
       # trans = str(raw_input("What would you like to see; Withdrawals(W) or Deposits(D)? ")).upper()
        # if trans == "W":
         #   print  "Here is a list of your transactions: "
          #  for i in W:
           #     print str(i) # printing as a string
                # calling the lists into view here.
        # elif trans == "D":
         #   print "Here is a list of your transactions: "
          #  for i in D:
           #     print str(i) # printing as a string
        # else:
         #   print "Str, please." # hard coded value check
    # except ValueError:
       # print("Str, please.")
        
            
# PROGRAM : numbered for #1 to 2#

os.system('cls') 
login() # 1
os.system('cls') # keeping the one menu on there (apart from withdrawals)

print "-" * 25
print "MENU"

def menu():
    choices =     [ "  ____________________  ",
                    " |                    | ",
                    " | DEPOSIT :      [D] | ",
                    " | WITHDRAW :     [W] | ",
                    " | BALANCE :      [B] | ",
                    " | TRANSACTIONS : [T] | ",
                    " | EXIT:          [E] | ",
                    " |____________________| ",
                   ]

    # placed my menu into a list, as this was the easiest an most accurate way, I found, to display it across different window sizes.
    
    for i in choices:
          print i # printed the list as a stack

    print ""
    print "-" * 25
    print "WELCOME : ", user_id.title() # printed the user_id with a capital first letter... OCD

menu() #2

def bank_system():

    
    print "-" * 25
    
    choice = raw_input("SELECTION: ")
    

    
    
    if choice == "D":
        deposit() # calling function.
        os.system('cls') # clear for OCD and nicer user interface
        print "Your new balance is : $ ", d_new_bal # printed balance using global variable
        menu() # recall menu options to keep them onscreen
        bank = True # bank system loop
        
    elif choice == "W":
        withdraw()
        # unable to replicate the above with deposit. Specifically with making "Insufficient Funds appear". The one way to do it would be to build the function
        # within this location. However, this would cause problems for global variables/function orders.
        # JAMES - would love to hear whether you can find a solution to this problem I had. I know you've got lots of submissions to look through so, if you find
        # the time it would be great to hear back from you.
        menu() 

        bank = True
        
    elif choice == "B":
        bank = True
        os.system('cls')
        with open(user_id + '.txt', 'r') as f:
            # opened using global variable user_id
            data = f.readlines()
            # added all the data into a list again
            print "BALANCE: $ ", data[1], "@", time_stamp
            # printed the balance using the second position in the list along with the time stamp for added value.
            print "-" * 25 
        menu()
        
    elif choice == "T":
        transactions()
        menu()
        # called the transactions function here
        
        bank = True

    elif choice == "E":
        os.system('cls')
        print "Goodbye"
        raise SystemExit()
        # raised a system exit to close the program. Exit message included.

        bank = False

    else:
        print "Please select one of the five choice from the menu"

        # hard coded error check, instead of ValueErrors etc.

while bank == True:
    bank_system() # the bank system loop :)


''' Hi James

I really enjoyed this project, I found it quite straight forward on the grand scheme of things in respect to what you've taught us. Had I not just had a very
busy last few weeks, I would have gladly finished level 3. It's been hectic and whilst I'm disappointed in not reaching level 3, I'm very happy with what I've
achieved above and look forward to wowing you with my SQL skills next semester.

Cheers.

Keith '''

