import pickle
import time
import win32api
import win32print
import getpass
#this allows the use of password encriptions
import os
#this allows give phthon the access required to save,input and delete information as required in the scipt
import sys
#this import allows me to make use of the sys.exit funtion which closes the program when the criteria is met
import time
#this allows the use of the sleep fucton which acts like a pause before the next function       

account_details = {}
is_logged_in = False
logged_in_user = ""

def display_balance(username):
    global account_details
    if is_logged_in == True :
        print 'Balance for ' + username + ' is ' + str(account_details[username]['Balance'])
        

def Account_Page():
    global is_logged_in
    global logged_in_user
    global account_details
    Pickle(account_details,'customer_dict')
    os.system('cls')
    print("Welcome " + logged_in_user + ", nice to see you again.")
    print("*********************************")
    print("What would you like to do today?")
    print("*********************************")
    print("[1] Check Balance")
    print("*********************************")
    print("[2] Add funds")
    print("*********************************")
    print("[3] Remove funds")
    print("*********************************")
    print("*********************************")
    print("[4] Print Balance")
    print("*********************************")
    print("[5] Logout")
    print("*********************************")        
    option = raw_input("Please select an option: ")

    if option == "1":
        os.system('cls')
        derp = unichr(163)
        statement_file = open("C:/Users/Public/Documents/statement_" + logged_in_user + "-" + time.strftime('%d-%m-%Y') + ".txt","a")
        statement_file.write("[" + time.strftime('%H-%M-%S') + "]Current Balance: " + derp.encode('latin-1') + str(account_details[logged_in_user]['Balance']) + "\n")
        statement_file.close()
        print "******************************"
        print("You currently have " + unichr(163) + str(account_details[logged_in_user]['Balance']) + " in your bank account.")
        print "******************************"
        raw_input("Press enter to continue")
        Account_Page()
        
    elif option == "2":
        os.system("cls")
        derp = unichr(163)
        print("How much would you like to add?")
        print ""
        add_fund = (raw_input("--> "))
        if add_fund.isdigit():
            add_fund = int(add_fund)
            if add_fund > 0:
                account_details[logged_in_user]["Balance"] += add_fund
                print("*********************************")
                print("Current balance is now " + unichr(163) + str(account_details[logged_in_user]['Balance']))
                statement_file = open("C:/Users/Public/Documents/statement_" + logged_in_user + "-" + time.strftime('%d-%m-%Y') + ".txt","a")
                statement_file.write("[" + time.strftime('%H-%M-%S') + "]Added " + derp.encode('latin-1') + str(add_fund) + " | Current Balance: " + derp.encode('latin-1') + str(account_details[logged_in_user]['Balance']) + "\n")
                statement_file.close()
                Account_Page()
            else:
                print("Cannot add negative numbers, try again")
                Account_Page()
        else:
            print("You must enter a number... ")
            
    elif option == "3":
        os.system('cls')
        derp = unichr(163)
        print("How much would you like to remove?")
        rmv_fund = int(raw_input("--> "))
        if account_details[logged_in_user]['Balance'] - rmv_fund < -100:
            os.system('cls')
            print("You currently don't have enough funds for this transaction")
            print("")
            raw_input("Press enter to continue")
        else:
            if rmv_fund > 0:
                account_details[logged_in_user]['Balance'] -= rmv_fund
                time_nsfw = time.strftime('%d-%m-%Y')
                time_safe = time_nsfw.encode('ascii','ignore')
                statement_file = open("C:/Users/Public/Documents/statement_" + logged_in_user + "-" + time_safe + ".txt","a")
                statement_file.write("[" + time.strftime('%H-%M-%S') + "]Removed " + derp.encode('latin-1') + str(rmv_fund) + " | Current Balance: " + derp.encode('latin-1') + str(account_details[logged_in_user]['Balance']) + "\n")
                statement_file.close()
                print("*********************************")
                print("Current balance is now " + unichr(163) + str(display_balance(logged_in_user)))
                print ""
                Account_Page()
            else:
                raw_input("You currently don't have enough funds for this transaction")
                Account_Page()
            
    elif option == "4":
        win32api.ShellExecute(
            0,
            "print",
            "C:/Users/Public/Documents/statement_" + logged_in_user + "-" + time.strftime('%d-%m-%Y') + ".txt",
            '/d:"%s"' % win32print.GetDefaultPrinter (),
            ".",
            0)
        
    elif option == "5":
        print("Thank you for stopping by " + logged_in_user)
        logged_in_user = ""
        is_logged_in = False
        raw_input("Press enter to continue")
        print ""
        os.system('cls')
        p()
    else:
        print("Incorrect option")
        Account_Page()


def Login():
    attempts = 0 
    loop = "true"
    global is_logged_in
    global logged_in_user
    global account_details
    test_pass = True
    while (loop == "true"):
        if attempts < 3:
            print "*********************************"
            print "Please Login to Access your Account"
            print "*********************************"
            print ""
            Username = raw_input("Please Enter A Username: ")
            Password = raw_input("Please Enter The Password: ")
            try:
                passwd = str(account_details[Username]['Password'])
            except:
                print("Incorrect username")
                attempts += 1
                test_pass = False

            if test_pass == True:
                if Password == passwd:
                    is_logged_in = True
                    logged_in_user = Username
                    Account_Page()
                    loop = "false"
                else:
                    print("Incorrect password")
                    attempts+=1
        else:
            print("You've attmpted the maximum number of attempts, you will now be returned to the main menu")
            p()
    p()
            

def Register():
    loop = "true"
    global account_details
    while loop == "true":
        CreateUser = raw_input("Please Enter Your Name: ")
        isEmpty = account_details.get(CreateUser, "empty")
        if(isEmpty != 'empty'):
            print ("username is already exists please select another name")
            Register()
        else :
            CreatePass = raw_input("Please Enter Your Password: ")
            account_details[CreateUser] = {}
            account_details[CreateUser].setdefault('Password', CreatePass)
            account_details[CreateUser].setdefault('Balance', 0.0)
            Pickle(account_details,'customer_dict')
            print "**********************************"
            print("User has been created, please login")
            loop = "false"
            print "**********************************"
            print ""
            Login()
            p()

def Pickle(custdict, filename):
    with open(filename,'wb') as handle:
        pickle.dump(custdict, handle)

def UnPickle(filename):
    with open(filename,'rb') as handle:
        custdict = pickle.load(handle)
    return custdict
        
def Quit(option):
    print "Goodbye"
    sys.exit()
        

#the below time.sleep function waits for 5 sececonds before the start of the next program

def p():
    global account_details
    if os.path.exists('customer_dict'):
        account_details = UnPickle('customer_dict')
    if is_logged_in == False:
        print "Welcome To GDI Banking Group!!"
        print "*****************************"
        time.sleep(1)
        print "Where you are always Number One!"
        time.sleep(1)
        #below is the script which allows the use to make choices withtin "Deposit money to the account, Withdraw money, Display the current balance, Display previous transactions.
        print "What Would you like to do today? "
        print ""
        print"******************************"
        print "[1] Login"
        print "*****************************"
        print ""
        print "*****************************"
        print "[2] Register"
        print "*****************************"
        print ""
        print "*****************************"
        print "[3] Quit"
        print "*****************************"


        #option 1 will be coded to allow the opening of a text file as logn as it atches the entered customer name.
        option = raw_input("Please Select an option: ")
        if option == "1":
            option = ""
            Login()
        elif option == "2":
            option = ""
            Register()
        elif option == "3":
            option = ""
            exit()
        else:
            print "Plese Select a Correct option"
            p()
    else:
        Account_Page()

if is_logged_in == False:
    p()
else:
    Account_Page()
