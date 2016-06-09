######################################################
#                                                    #
# Semester 1 Project, Week 10, Programming in Python #
# Coding a Bank account simulation                   #
# Andreas Georgiou                                   #
#                                                    #
######################################################

import os # Imports the os library enabling me to clear the previous options the user has carried out from the display.
import hashlib # Imports the hash library enabling the use of ciphering strings.
import sys # Imports the system library enabling the use of systems functions sych as exiting the program (sys.exit())
import time # Imports the time library enabling the use of printing out the date and/or time in chosen formats.

class login(): # Creates class that contains methods for the first part of the internet banking program, such as displaying the header and logging the user in.
    def header(self):
        print "\n", """
     _____   ____   _               
    / ____| |  _ \ | |     
   | |  __  | |_)| | |      
   | | |  | |   <  | |
   | |__| | | |_)| | |____ 
    \_____| |____/ |______|  Banking Group """, "\n","\n" # Prints the GBL Banking Group header, "\n" leaves a gap.
        
    def log_in(self): # Defines a method that logs a user into their account depending on their credentials, comparing their input to data stored in .txt files.
        options1 = options()
        login1 = login()
        pw_file = open("passwordmd5.txt", "r") # Opens the 'passwordmd5.txt' file ready to be read and stores it in 'pw_file' variable.
        store = pw_file.read() # Stores the data from the opened .txt file to the 'store' variable. 
        pw_file.close() # Closes the opened .txt file as it is no longer needed because the data from it was stored in a variable.
        # The users passwords were md5 ciphered and stored in a text file. The above code openes the text file and stores the ciphered password in
        # a variable, ready to be used by the program. For test reasons both users have the same password.
        
        auser_file = open("auser.txt", "r")
        global auser # Changes 'auser' to a global variable so it can be accessed by other methods and classes in the program.
        auser = auser_file.read()
        auser_file.close()
        # The username was stored in a text file. The above code openes the text file and stores the user id in a variable
        # ready to be used by the program.
        
        puser_file = open("puser.txt", "r")
        global puser
        puser = puser_file.read()
        puser_file.close()
        
        print "Log on    (Leave blank to exit)", "\n", "---"
        global user_id
        user_id = raw_input("User ID   : ").title() # Allows the user to enter their user id.
        pw_entry = raw_input("Password  : ") # Allows the user to enter their password.
        md5_pw = hashlib.new("md5") # Creates a variable with the md5 hash library stored inside ande ready to use.
        md5_pw.update(pw_entry) # Ciphers the users password input into md5 format.
        if md5_pw.hexdigest() == store and user_id == auser:
            os.system('cls') # Clears the previous options the user has carried out from the display.
            login1.header()
            print "\n", "*Welcome to Internet Banking*", "\n" # If statement that checks if the md5 version of the users password input is the same as the password
                                                            # stored in the text file, AND the user id input by the user is also the same as the user id stored in
                                                            # the text file. If it is, then the user will be authenticated and the welcome message will be displayed.
            options1.menu() # Prints out the menu.
        elif md5_pw.hexdigest() == store and user_id == puser:
            os.system('cls')
            login1.header()
            print "\n", "*Welcome to Internet Banking*", "\n"
            options1.menu()
        elif user_id == "" and pw_entry == "":
                print "\n", "*Internet banking exited*" # Exits internet banking if the user leaves the user_id and password field blank.
                sys.exit()
        else:
            os.system('cls')
            login1.header()
            print "\n", "*Incorrect User ID or Password. Enter correct login information*", "\n"
            login1.log_in()
            # If the password OR the user id entered by the user does not match the data in the password/user id text files, then the user
            # will not be authenticated and the incorrect user id or password message will be displayed. The log_in method will then run
            # meaning the user will then be promted to re-enter the user id and password.


class options():
    def menu(self): # Prints out a list that displays the menu for the internet banking application and a short description of what the menu options do.
        
        print "-" * 15
        main_menu = [">[1] Balance          *View current balance",
                     ">[2] Statement        *View this months transactions",
                     ">[3] Deposit          *Make a deposit",
                     ">[4] Withdraw         *Make a withdrawal", " ",
                     ">[5] Options          *Re-display options menu",
                     ">[6] Logout           *Log out of internet banking",
                     ">[7] Exit             *Exit internet banking", "\n",]
        for w in main_menu:
            print w

class actions(login): # Creates class that contains methods for all the various actions a user can perform. Also inherits the 'login' class.
    def view_astat(self): # Prints the users statement using data stores in the statement text file.
        month_stamp = time.strftime("%B")
        astat_l = ""
        astat_file = open("astat.txt", "r") # Opens the text file containing the users recent transactions statement.
        for line in astat_file:
            astat_l += line # A for loop that runs through each line of the text file and stores it to the astat_1 variable.
        print "\n", month_stamp, "Statement", "\n", "---", "\n", astat_l # Prints the data from the statement text file.
                                                                         # This is done by adding the data from the text file line by line to the
                                                                         # 'astat_1' variable then printing the variable. 

    def view_pstat(self):
        month_stamp = time.strftime("%B")
        pstat_l = ""
        pstat_file = open("pstat.txt", "r")
        for line in pstat_file:
            pstat_l += line
        print "\n", month_stamp, "Statement", "\n", "---", "\n", pstat_l

    def view_abal(self):
        abal_file = open("abalance.txt", "r") # Prints the users balance.
        global abal_1
        abal_1 = abal_file.read()
        print "\n", "Current balance    $", abal_1
        print "Avaliable balance  $", int(abal_1) + 100
        # Opens the text file containing the users balance and stores it in a variable. The balance is then printed twice; once for the users actual balance
        # and a second time of the users balance plus 100 which is added as the user has a $100 overdraft.
        
    def view_pbal(self):
        pbal_file = open("pbalance.txt", "r")
        global pbal_1
        pbal_1 = pbal_file.read()        
        print "\n", "Current balance    $", pbal_1
        print "Avaliable balance  $", int(pbal_1) + 100
        
    def update_balance_dep(self): # A method that allows the user to deposit money into their account and updates the balance after money has been deposited.
        menu_all = actions()
        choose = select()
        time_stamp = time.strftime("%d%b%y,%H:%M:%S")
        try:
            deposit_amount = int(raw_input(">Amount to deposit: ")) # Allows the user to input the amount they would like to deposit. The digit they input
                                                                    # is converted to an integer.
            print "*Deposit successful*"
            if user_id == auser: # This if statement will be used if the user logged in is the same user details stored in the file 'auser.txt'.
                total = deposit_amount + int(abal_1) # Converts the string(balance) stored in the 'abal_1' global variable into an integer,
                                                      # then adds the users input(the amount they want to deposit) to the current balance.
                                                      # The total in then stored in the 'total' variable.
                with open("abalance.txt", "w") as f:
                    f.write(str(total)) # The current balance(the integer stored in 'total') is then written back to the text file that stores the balance.
                with open("astat.txt", "a") as f:
                    f.write("\n" + "deposit" + time_stamp + "........." + str(deposit_amount)) # Appends the deposit made to the associated text file
                                                                                             # to show the users statement.
                menu_all.view_abal() # Runs the view.abal() method which displays the users up to date balance.
                print "-" * 15
                choose.selection() # Runs the selection() method which allows users to choose what actions they with to take on their bank account.
            elif user_id == puser: # This elif statement will be used if the user logged in is the same user details stored in the file 'puser.txt'.
                total = deposit_amount + int(pbal_1)
                with open("pbalance.txt", "w") as f:
                    f.write(str(total))
                with open("pstat.txt", "a") as f:
                    f.write("\n" + "deposit" + time_stamp + "........." + str(deposit_amount))
                menu_all.view_pbal()
                print "-" * 15
                choose.selection()
        except ValueError: # An exception that runs if the user inputs a letter or any decimal points. A notification is printed that prompts the user
                           # to enter a whole number only, then the update_balance_dep() method is re-run to allow them to retry.
            print "\n", "*Please deposit a whole currency amount only*"
            choose = select()
            choose.selection() 

    def update_balance_with(self): # A method that allows the user to withdraw money from their account and updates the balance after money has been withdrawn.
        menu_all = actions()
        choose = select()
        time_stamp = time.strftime("%d%b%y,%H:%M:%S") # Stores the date and time in a variable.
        try:
            deposit_amount = int(raw_input(">Amount to withdraw: ")) # Allows the user to input the amount they would like to withdraw.
                                                                      # The digit they input is converted to an integer.
            if user_id == auser: # This if statement will be used if the user logged in is the same user details stored in the file 'auser.txt'.
                total = int(abal_1) - deposit_amount # Converts the string(balance) stored in the 'abal_1' global variable into an integer,
                                                      # then subtracts the users input(the amount they want to withdraw) from the current balance.
                                                      # The total in then stored in the 'total' variable.
                if total >= -100: # As the users have been provided with 100 overdraft, this if statement checks to see if the total exceedes -100.
                                  # If it does exceed, then the user is promted to re-enter an amount they with to withdraw and is notified of
                                  # insufficinet funds. If it does not exceed -100 then the if statement will run.
                                  
                    with open("abalance.txt", "w") as f:
                        f.write(str(total)) # The current balance(the integer stored in 'total') is then written back to the text file that stores the balance.
                    with open("astat.txt", "a") as f:
                        f.write("\n" + "withdraw" + time_stamp + "........" + str(deposit_amount)) # Appends the withdrawal made to the statement text file
                                                                                                   # to show on the users statement. Also includes the date
                                                                                                   # and time.
                    menu_all.view_abal() # Runs the view.abal() method which displays the users up to date balance.
                    print "-" * 15
                    choose.selection() # Runs the selection() method which allows users to choose what actions they with to take on their bank account.
                else: 
                    print "*Insufficient funds to proceed with transaction*"
                    menu_all.view_abal()
                    print "-" * 15
                    choose.selection()
            elif user_id == puser: # This elif statement will be used if the user logged in is the same user details stored in the file 'puser.txt'.
                total = int(pbal_1) - deposit_amount
                if total >= -100:
                    with open("pbalance.txt", "w") as f:
                        f.write(str(total))
                    with open("pstat.txt", "a") as f:
                        f.write("\n" "withdraw" + time_stamp + "........" + str(deposit_amount))
                    menu_all.view_pbal()
                    print "-" * 15
                    choose.selection()
                else:
                    print "*Insufficient funds to proceed with transaction*"
                    menu_all.view_abal()
                    print "-" * 15
                    choose.selection()
        except ValueError: # An exception that runs if the user inputs a letter or any decimal points. A notification is printed that prompts the user
                           # to enter a whole number only, then the update_balance_with() method is re-run to allow them to retry.
            print "\n", "*Please deposit a whole currency amount only*"
            choose = select()
            choose.selection()

class select(login): # This class contains a method, that runs certain other methods depending on the users input.
    def selection(self):
        menu_all = actions()
        choose = select()
        login1 = login()
        options1 = options()
        print ""
        view = raw_input(">Select menu option to continue: ").lower() # Allows the user to input their choice of actions to perform on their bank account.
                                                                    # The user input is converted to lower case, therefore it makes no difference how the
                                                                    # user chooses to type their menu option.
        os.system('cls') # Clears the previous options the user has carried out from the display.
        if user_id == auser and (view == "statement" or view == "2"):
            # If the user_id matches the same user_id in the text file, and the user selects 'statement', the method runs that
            # displays the statement for that user.
            login1.header() # Displays the internet banking application header.
            options1.menu()
            menu_all.view_astat()
            print "-" * 15
            choose.selection()
        elif user_id == puser and (view == "statement" or view == "2"):
            login1.header()
            options1.menu()
            menu_all.view_pstat()
            print "-" * 15
            choose.selection()
        elif user_id == auser and (view == "balance" or view == "1"):
            # If the user_id matches the same user_id in the text file, and the user selects 'balance', the method runs that
            # displays the balance for that user.
            login1.header()
            options1.menu()
            menu_all.view_abal()
            print "-" * 15
            choose.selection()
        elif user_id == puser and (view == "balance" or view == "1"):
            login1.header()
            options1.menu()
            menu_all.view_pbal()
            print "-" * 15
            choose.selection()
        elif user_id == auser and (view == "deposit" or view == "3"):
            # If the user selects 'deposit', the method runs that allows the user to deposit money in their account.
            login1.header()
            options1.menu()
            menu_all.view_abal()
            menu_all.update_balance_dep()
            choose.selection()
        elif user_id == puser and (view == "deposit" or view == "3"):
            # If the user selects 'deposit', the method runs that allows the user to deposit money in their account.
            login1.header()
            options1.menu()
            menu_all.view_pbal()
            menu_all.update_balance_dep()
            choose.selection()
        elif user_id == auser and (view == "withdraw" or view == "4"):
            # If the user selects 'withdraw', the method runs that allows the user to withdraw money from their account.
            login1.header()
            options1.menu()
            menu_all.view_abal()
            menu_all.update_balance_with()
            choose.selection()
        elif user_id == puser and (view == "withdraw" or view == "4"):
            # If the user selects 'withdraw', the method runs that allows the user to withdraw money from their account.
            login1.header()
            options1.menu()
            menu_all.view_pbal()
            menu_all.update_balance_with()
            choose.selection()
        elif view == "5":
            # If the user selects 'return', the option menu is displayed.
            login1.header()
            options1.menu()
            print "-" * 15
            choose.selection()
        elif view == "logout" or view == "6":
            # If the user selects 'logout', the user is logged out and the programs goes back to the login page where another user can log on.
            login1.header()
            print "*Logged out, see you again soon*", "\n"
            login1.log_in()
            choose.selection()
        elif view == "exit" or view == "7":
            # If the user selects 'exit', the program ends.
            print "\n", "*Internet banking exited*"
            sys.exit()
        else:
            # If the user selects and invalid options, a message is displayed promting them to re-enter and they are able to try again.
            login1.header()
            print "\n", "*Menu option not valid*"
            options1.menu()
            print "-" * 15
            choose.selection()
  
login1 = login()
login1.header() # Prints the GBL banking Group header.
login1.log_in() # Runs the login method.

choose = select()
choose.selection() # Allows the user to make a selection from the menu.
