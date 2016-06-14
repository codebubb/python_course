from datetime import datetime
import sys
now = datetime.now()
now_2 = "%s/%s/%s %s:%s:%s" % (now.day, now.month, now.year, now.hour, now.minute, now.second)

print "* * * * * * * * * * * * * * * * *"
print "* Welcome to GBL Banking Online *"
print "*  You will now need to login!  *"
print "* * * * * * * * * * * * * * * * *\n"

class GBL_Banking():        

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        with open(self.username +".txt", 'r') as f:
            stored_username = f.readline()
            stored_password = f.readline()
        if self.username == stored_username.strip() and self.password == stored_password.strip():
            return False
            
        else:
            print "Wrong Username or Password."
            login_attempts += 1

    def menu(self):
        
        print "***********************************************************"
        print "Welcome", self.username,"to your Online GBL Banking portal.\n"
        print "Here is the main menu. Please select an option below:"
        print "[1] Make a Deposit.----------------------------------------"
        print "[2] Make a Withdrawal.-------------------------------------"
        print "[3] View Balance.------------------------------------------"
        print "[4] Mini Statement (Last 5 Transactions).------------------"
        print "[5] Full Statement.----------------------------------------"
        print "[6] Log out.-----------------------------------------------"
        print "***********************************************************"
        overdraft = 100
        choice = raw_input()
        if choice == "1":
            deposit_amount = raw_input("How much would you like to deposit? $")
            try:
                with open(self.username +".txt", 'r') as f:
                    lines = f.readlines()
                    current_balance = lines[2].strip()
                    updated_balance = int(current_balance) + int(deposit_amount)
                    lines[2] = str(updated_balance)+"\n"
                    print "\nDeposit made. \nCurrent Balance:", "$" + str(updated_balance)
                    bal_inc_overdraft = int(updated_balance) + overdraft
                    print "Available Balance:","$"+ str(bal_inc_overdraft), " \n"
                with open(self.username +".txt", 'w') as f:
                    lines.insert(3, now_2+' Cash Deposit: '+deposit_amount+' '+ str(updated_balance)+'\n')
                    f.writelines( lines )
                self.menu()
            except ValueError:
                print "\nPlease only enter whole numbers.\n"
                self.menu()
                
                

        elif choice == "2":
            withdrawal_amount = raw_input("How much would you like to withdraw? $")
            try:
                with open(self.username +".txt", 'r') as f:
                    lines = f.readlines()
                    current_balance = lines[2].strip()
                    if int(current_balance) - int(withdrawal_amount) < -100:
                        print "\nYou only have", "$" + str(current_balance), "in your account."
                        bal_inc_overdraft = int(current_balance) + overdraft
                        print "\n$"+ str(bal_inc_overdraft), "including your $100 overdraft.\n"
                        self.menu()
                    else:
                        updated_balance = int(current_balance) - int(withdrawal_amount)
                        lines[2] = str(updated_balance)+"\n"
                        print "\nWithdrawal made. \nCurrent Balance:", "$" + str(updated_balance)
                        bal_inc_overdraft = int(updated_balance) + overdraft
                        print "Available Balance:", "$"+ str(bal_inc_overdraft), " \n"
                with open(self.username +".txt", 'w') as f:
                    lines.insert(3, now_2+' Cash Withd.: -'+withdrawal_amount+' '+ str(updated_balance)+'\n')
                    f.writelines( lines )
                self.menu()
            except ValueError:
                print "\nPlease only enter whole numbers.\n"
                self.menu()

            
        elif choice == "3":
            with open(self.username +".txt", 'r') as f:
                lines = f.readlines()
                balance = lines[2].strip()
                f.close()
                print "\nCurrent Balance:", "$" + str(balance)
                bal_inc_overdraft = int(balance) + overdraft
                print "Available Balance:", "$"+ str(bal_inc_overdraft), " \n"
                self.menu()


        elif choice == "4":
            print "Here is your most up to date Mini Statement:\n"
            print "Date/Time         In/Out        $  Balance\n"
            with open(self.username +".txt", 'r') as f:
                lines = f.readlines()
                for e in lines[3:8]:
                    print e
                self.menu()

        elif choice == "5":
            print "Here is your most up to date Statement:\n"
            print "Date/Time         In/Out        $  Balance\n"
            with open(self.username +".txt", 'r') as f:
                lines = f.readlines()
                for e in lines[3:]:
                    print e
                self.menu()

        elif choice == "6":
            sys.exit()

        else:
            print "\nPlease enter a number 1-5\n"
            self.menu()

login_attempts = 0
while True:
    try:
        if login_attempts < 3:
            new_user = GBL_Banking(raw_input("Please Enter a username: "), raw_input("Please Enter a password: "))
            new_user.login()
            if new_user.login() == False:
                print "Login Completed.\n"
                new_user.menu()
                break
        else:
            print "You have succeeded the amount of Login attempts. Please go to your local branch."
            break
    except IOError:
        print "Wrong Username or Password."
        login_attempts += 1
    except UnboundLocalError:
        login_attempts += 1








        
