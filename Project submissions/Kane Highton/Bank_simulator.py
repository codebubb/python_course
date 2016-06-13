

import time
import os
import sys

time = time.strftime("%d-%m-%y at %H:%M:%S") #records the time and date of transactions made


bank = True

options = ["Deposit money [1]" , "Withdraw money [2]" , "Display current balance [3]" ,
            "Display previous transactions [4]", "Log off [5]"] #options given to the user to choose from

d = []
w = []


def login(): #options given to the user when they run the program
    global userid
    while True:
        try:
            user = str(raw_input("Are you a new or existing customer?: "))
            if user == 'new':
                userid = raw_input("please enter the user ID you want to use: ") #users' choice of ID
                # new_user = 'newuser.txt' <- Don't need this if we've already got the userid for the filename - James.
                open_file = open(userid + ".txt" , 'a+') #reads and appends users' input to the blank 'new user' .txt file
                open_file.write(userid + '\n')
                userPin =(raw_input("Please create a pin (4 digits only): ")) #users' choice of a pin
                # new_user = 'newuser.txt' <- see above comment - James
                # open_file = open(new_user + ".txt" , 'a+') <- File is already open - James    #reads and appends users' input to the 'new user' .txt file
                open_file.write(userPin)
                open_file.close
                print " "
                print "Welcome to GBL banking. "
                break



            if user == 'existing':
                userid = str(raw_input("Please enter you User ID: "))
                with open(userid + ".txt", "r") as f:#looks for the file titled the users' ID and reads i
                    pin = raw_input("what is your pin?: ")
                    if pin == f.readline().strip():#reads the first line of the file to ensure pin matches
                        print "welcome " + f.readline() #reads users' full name from file
                        break
                    else:
                        print "Incorrect pin entered too many times. Please try again."


        except ValueError:
            print "Please enter a valid input."




def option(): #Prints the options the user has to choose from
    print " "
    for opt in options:
        print "*" , opt


def deposit(): #the options given to the user to deposit

    global userid

    while True:
        try:
            amount = int(raw_input("Please enter how much you'd like to deposit ($1000 max.) "))
            if amount > 1000:
                print "Amount too large to deposit."
            else:

                # Not sure what this is trying to do here? I got an IndexError when running the program - James.
                with open(userid + ".txt" , "r") as f:
                    lines = f.readlines()
                    new_amount = int(lines[2]) + amount #Adds the amount the user deposits to current amount
                    dep_time = "$" + str(amount) + " On " + time #Saves this transaction to later be recalled when looking at transactions
                    d.append(dep_time)

                print "Thank you. Depositing %s now." % str(amount)


                with open(userid + ".txt" , "r") as f:
                    lines = f.readlines()
                    lines[2] = str(new_amount) #updates to new balance after deposit

                with open(userid + ".txt" , "w") as f:
                    f.writelines(lines)
                    break
        except ValueError:
            print "Please enter a valid number."

def overdraft(): #allows the user to go into an overdraft if they want to withdraw more money than they have available

    global with_balance

    with open(userid + ".txt" , "r") as f:
        lines = f.readlines()
    option = raw_input("""
You are about to go into your overdraft. Do you want to do this?:
1) Yes
2) No
""")

    if option == "yes":
            with open(userid + ".txt" , "r") as f:
                lines = f.readlines() #reads the users personal file
                with_balance = int(lines[2]) - wit_amount #takes the amount from their amount
                with_time = "$" + str(withdraw) + " On " + time #saves the data to be re-read when looking at transactions
                w.append(with_time)
            print "Okay. Withdrawing $ %s for you." % wit_amount

    elif option == "no":
        print "Sorry. Insufficient funds available."

def withdraw():
    try:
        global wit_amount
        wit_amount = int(raw_input("How much would you like to witdraw? ($10 min - $1000 max.): "))
        if wit_amount > 1000:
            print "Amount too large to withdraw."

            global new_bal

        else:
            with open(userid + ".txt" , "r") as f:
                amount = f.readlines()
                if int(amount[2]) - wit_amount < -1: #if the requested amount goes into negatative - will run the overdraft() functions
                    overdraft()

                else:
                    with open(userid + ".txt" , "r") as f:
                        amount = f.readlines()
                        new_bal = int(amount[2]) - wit_amount
                        wit_update = "$" + str(wit_amount) + " On " + time #saves the amount/date/time so can be re read by user
                        w.append(wit_update)
                        print " "
                        print "Thank you. withdrawing %s from your account." % wit_amount

                        with open(userid + ".txt" , "r") as f:
                            amount = f.readlines()
                            amount[2] = str(new_bal)

                        with open(userid + ".txt" ,"w") as f:
                            f.writelines(amount) #writes the new balance to .txt file


    except ValueError:
        print "Please enter an amount to withdraw."




def balance():

    with open(userid + ".txt" , "r") as f:
        amount = f.readlines()

        print " "
        print "Your current balance is: $ ", amount[2] #reads 3rd line of users account which is balance and prints



def transactions():

    try:
        user_trans = str(raw_input("Would you like to see a)Deposit or b)Withdraw transactions?: "))
        if user_trans == "a":
            print """
\n
--------------- Last Deposits  -----------------
"""
            for i in d:
                print "          " , str(i)  #after any deposits have been stored, this will print them out to user
                print """

---------------- GBL Bank PLC ------------------
"""

        elif user_trans == "b":
            print """
\n
--------------- Last Withdraws -----------------
"""

            for i in w:
                print "          " , str(i)   #save as above, however with withdraws
                print """

---------------- GBL Bank PLC -----------------
"""

    except ValueError:
        print "Please enter a correct answer."
        transactions()



### MAIN CODE ###


os.system('cls')
print " "
print "Hello, and welcome to the GBL online banking system."
print " "
login()

option()
print " "



def main_bank_sys(): #Runs the whole code through the 'if' statements


    choice = raw_input("Please choice from the above what you would like to do: ")
    if choice == "1":
        deposit()
        bank = True
    if choice == "2":
        withdraw()
        bank = True
    if choice == "3":
        balance()
        bank = True
    if choice == "4":
        transactions()
        bank = True
    if choice == "5":
        os.system('cls')
        print "Thank you for using GBL Online Banking System."
        print "Logging off."
        raise SystemExit()

        bank = False


while bank == True:
    main_bank_sys()
