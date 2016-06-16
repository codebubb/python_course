import hashlib
import time
import os
def cls():
    print ('\n' * 10)
def cls_b():
    print ('\n' * 25)

class Bank_account(object):
    # Main bank acount class

    global username
    username = []
    #Created a global variable for username so that when a new user is created or and old
    #user logs in the username is appended here

    def __init__(self,balance = 0):
        self.balance = balance
    #Initial starting balance for the account is zero

    def account_create(self):
        userid = raw_input('Please create a user name\nThis will be your login ID: ')
        username.append(userid)
        # Above takes the users input and appends it to the global variable username
        with open(userid + '.txt', 'w') as f:
            user = hashlib.md5()
            user.update(userid)
            f.write (user.hexdigest() + '\n')
            pin = hashlib.md5()
            pin.update(raw_input('Please create a password\nThis will be your password to login:  '))
            f.write(pin.hexdigest())
            f.close()
        # Takes both the users input for username and there password, runs it through a hash and writes that to the main file
        with open(userid + 'balance.txt', 'w') as f:
            f.write (str(self.balance))
        # creates a balance file for the users account
        with open(userid + 'transaction.txt', 'w') as f:
            f.close()
        #creates a transaction file for the users account
        # I found it much more simple to seperate these files instead of storing all the information on one file, also adds
        # a layer of security as not all a users infor is in one place ;)


    def login_check(self):
        while True:
            userid = raw_input('Please enter your user ID: ')
            username.append(userid)
            # when a user comes to log in there input is saved t the variable above and appened to the global variable username
            try:
                f = open(''.join(userid) + '.txt', 'r')
                # looks for the file with the users input plus the txt extention
            except IOError:
                print 'Username not found Please try again'
                del username[0]
                # if that file is not found the global variable is deleted at index 0, in other words the list is cleared
                # to prevent the wrong input creating a completely new file once the correct input is entered.
                continue
            else:
                with f:
                    x = f.readlines()
                    user_input = hashlib.md5()
                    user_input.update(userid)
                    pass_input = hashlib.md5()
                    pass_input.update(raw_input('Please enter your 4 digit pin: '))
                    if x[0] == user_input.hexdigest() + '\n' and x[1] == pass_input.hexdigest():
                        last_bal = open(''.join(username) + 'balance.txt', 'r')
                        lb = last_bal.readlines()
                        self.balance = int(''.join(lb[0]))
                        f.close()
                    # This checks that the user input matched the username and password that was hashed to the main file
                    # if that input, once hased does not match that in the file then the user will not be able to log in
                    else:
                        del username[0]
                        # if that happend once again the global variable list is cleared and the while loop is started again
                        print 'Your password is incorrect please try again'
                        continue
                break




    def deposit(self,amount):
        with open(''.join(username) + 'transaction.txt', 'a+') as f:
            x = f.readlines()
            f.write('\nDeposit ' + str(amount) + ' GPB on ' + time.strftime("%d:%m:%y") + ' at ' + time.strftime("%H:%M"))
            self.balance += amount
            f.close()
            #Every time a deposit is made it uses the global variable to find the correct users file, opens that file and writes the transaction
            #including the time and date stamp, amends the balance and closes the file
        with open(''.join(username) + 'balance.txt', 'w') as f:
            f.write (str(self.balance))
            f.close()
            #it also does the same to the balance txt file so all aspects of the account are kept up to date


    def withdraw(self,amount):
        if amount > self.balance:
            print '!!!!!You Have insufficient funds available!!!!!'
        else:
            with open(''.join(username) + 'transaction.txt', 'a+') as f:
                x = f.readlines()
                f.write('\nWithdrawal ' + str(amount) + ' GPB on ' + time.strftime("%d:%m:%y") + ' at ' + time.strftime("%H:%M"))
                self.balance -= amount
                f.close()
            with open(''.join(username) + 'balance.txt', 'w') as f:
                f.write (str(self.balance))
                f.close()
            # The withdraw function works the same as the deposit by writing to the transaction file every time a withdrawal is made
            # and also updating the balance to the balance txt, but includes the if statment so that if the amount that is being withdrawn is
            #more than the balance it will tell the user they have insufficient funds.

class Overdraft(Bank_account):

    def __init__ (self):
        Bank_account.__init__(self)


    def withdraw_o(self,amount):
        if amount > self.balance + 100:
            print'!!!!!You Have insufficient funds available!!!!!'
        else:
            with open(''.join(username) + 'transaction.txt', 'a+') as f:
                x = f.readlines()
                f.write('\nWithdrawal ' + str(amount) + ' GPB on ' + time.strftime("%d:%m:%y") + ' at ' + time.strftime("%H:%M"))
                self.balance -= amount
                f.close()
            with open(''.join(username) + 'balance.txt', 'w') as f:
                f.write (str(self.balance))
                f.close()


cust = Bank_account()
new_cust = Overdraft()

def main_screen_o():
    with open(''.join(username) + 'transaction.txt', 'r') as f:
                    x = f.readlines()
                    last_bal = open(''.join(username) + 'balance.txt', 'r')
                    lb = last_bal.readlines()
                    new_cust.balance = int(''.join(lb[0]))
                    f.close()




    print '''
____________________________________________________________________________
Welcome ''' + ''.join(username) + '''
Your current balance is ''' + str(new_cust.balance) +''' GBP your overdraft is 100 GBP ''''''
your avalible balance is ''' + str(new_cust.balance + 100) + ''' GBP''''''
Please select from the follwing options

1. Make a deposit

2. Make a withdrawal

3. View all of your trainsactions

4. Remove your over draft (Must have avaible funds)

5. Log out
____________________________________________________________________________

|  Last 5 transactions  |
''' + ''.join(x[-5:]) + '''
'''
    while True:
        try:
            pick = int(raw_input('-- Enter your option number here: '))
            if pick == 1:
                new_cust.deposit(int(raw_input('Please enter amount to deposit: ')))
                cls_b()
                return main_screen_o()
                break
            elif pick == 2:
                new_cust.withdraw_o(int(raw_input('Please enter amount you wish to withdraw: ')))
                cls_b()
                return main_screen_o()
                break
            elif pick == 3:
                with open(''.join(username) + 'transaction.txt', 'r') as f:
                    x = f.readlines()
                    print ''.join(x)
                    f.close()
                    return main_screen_o()
            elif pick == 4:
                a = str(raw_input('Do you with to remove your overdraft y/n: '))
                if a.lower() == 'y':
                    if new_cust.balance >= 0:
                        os.remove(''.join(username) + 'overdraft.txt')
                        with open(''.join(username) + 'transaction.txt', 'a+') as f:
                            x = f.readlines()
                            f.write('\nOverdraft of 100 GBP removed on ' + time.strftime("%d:%m:%y") + ' at ' + time.strftime("%H:%M"))
                            f.close()
                            del username[0]
                            cls_b()
                            return opening()
                    else:
                         print '!!!!!You Have insufficient funds available to remove your overdraft!!!!!'
                if a.lower() == 'n':
                    cls_b()
                    return main_screen_o()

            elif pick == 5:
                    exit()
        except ValueError:
            print 'Please enter a number as amount'
            continue
        else:
            print 'Please try again'
            continue



def opening_o():

    print '''
____________________________________________________________________________
Please select one of the options
By typing the number below

1. login to your acount

____________________________________________________________________________
        '''
    while True:
        try:
            pick = int(raw_input('-- Enter your option number here: '))
        except ValueError:
            print 'Please select a number as an integer: '
            continue
        if pick == 1:
            new_cust.login_check()
            cls_b()
            return main_screen_o()
            break
        else:
            print 'Please try again'
            continue



def main_screen():

    with open(''.join(username) + 'transaction.txt', 'r') as f:
                    x = f.readlines()




    print '''
____________________________________________________________________________
Welcome ''' + ''.join(username) + '''
Your current balance is ''' + str(cust.balance) +''' GBP ''''''
Your avalible balance is ''' + str(cust.balance) + ''' GBP ''''''
Please select from the follwing options

1. Make a deposit

2. Make a withdrawal

3. View all of your trainsactions

4. Apply for an overdraft (100 GBP)

5. Log out
____________________________________________________________________________

|  Last 5 transactions  |
''' + ''.join(x[-5:]) + '''
'''
    while True:
        try:
            pick = int(raw_input('-- Enter your option number here: '))
            if pick == 1:
                cust.deposit(int(raw_input('Please enter amount to deposit: ')))
                cls_b()
                return main_screen()
                break
            elif pick == 2:
                cust.withdraw(int(raw_input('Please enter amount you wish to withdraw: ')))
                cls_b()
                return main_screen()
                break
            elif pick == 3:
                with open(''.join(username) + 'transaction.txt', 'r') as f:
                    x = f.readlines()
                    print ''.join(x)
                    f.close()
                    return main_screen()
            elif pick == 4:
                a = str(raw_input('Do you require a 100 GBP overdraft y/n: '))
                if a.lower() == 'y':
                    with open(''.join(username) + 'overdraft.txt', 'w') as f:
                        f.close()
                    with open(''.join(username) + 'transaction.txt', 'a+') as f:
                        x = f.readlines()
                        f.write('\nOverdraft of 100 GBP added on ' + time.strftime("%d:%m:%y") + ' at ' + time.strftime("%H:%M"))
                        f.close()
                        del username[0]
                        cls()
                        return opening_o()
                if a.lower() == 'n':
                    cls_b()
                    return main_screen()


            elif pick == 5:
                exit()
        except ValueError:
            print 'Please enter a number as amount'
            continue
        else:
            print 'Please try again'
            continue





def opening():

    print '''
____________________________________________________________________________
Please select one of the options
By typing the number below

1. Create a new account

2. login to your acount
____________________________________________________________________________
        '''
    while True:
        try:
            pick = int(raw_input('-- Enter your option number here: '))
        except ValueError:
            print 'Please select a number as an integer: '
            continue
        if pick == 1:
            cust.account_create()
            cls_b()
            return account_type()
            break
        elif pick == 2:
            cust.login_check()
            cls_b()
            return account_type()
            break
        else:
            print 'Please try again'
            continue
def account_type():
    try:
        with open(''.join(username) + 'overdraft.txt', 'r') as f:
            f.close()
            return main_screen_o()
    except IOError:
        return main_screen()



opening()
