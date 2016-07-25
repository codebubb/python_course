#user must be one of 3 accounts with PIN 1234, 8080 or 2468
#customer greeting depends on time of day#
def greeting():
    import time
    time = time.strftime('%H : %M : %S')
    if time > '12 : 00 : 00':
        print 'Good afternoon customer.'
    elif time > '18 :00 :00':
        print 'Good evening customer.'
    else:
        print 'Good morning customer.'

#welcomes correct customer and confirms account#
def welcome():
    pin = raw_input('Please insert you card and enter your PIN:  ')
    while pin == '1234':
        print '''
Welcome Taylor Swift
Account ****6263

'''
        break
    while pin == '8080':
        print'''
Welcome Justin Beiber
Account ****3019

'''
        break
    while pin == '2468':
        print '''
Welcome Kim Kardashian
Account ****9021

'''
        break
    if pin != '1234' and pin != '8080' and pin != '2468':
        print 'This is an invalid PIN'
        return welcome()

 #balance and transactions used as global variables#   
balance = 200
transactions = []

#customer chooses what action they want to take, repeats when each action completed#
def choice():
    global balance
    global transactions
    print '''1 - Withdraw money
2 - Deposit money
3 - View account balance
4 - View previous transactions
5 - Exit
'''
    action = raw_input('What would you like to do today?  ')
#withdrawn money chosen withdraws from balance, prints new balance and stores to transactions#
    while action == '1':
        withdraw_amount = raw_input('How much money would you like to withdraw today?  ')
        if float(withdraw_amount) > balance:
            print 'You have insufficient funds.'
        else:
            balance -= float(withdraw_amount)
            transactions.extend(['You withdrew $'+withdraw_amount])
            print 'You have withdrawn $',withdraw_amount, ' from your account. You now have $',balance, ' Thank you.'
        return choice()
        break
#deposit money chosen adds money to balance, prints new balance and stores to transactions#
    while action == '2':
        deposit_amount = raw_input('How much money would you like to deposit today?  ')
        balance += float(deposit_amount)
        transactions.extend(['You deposited $'+deposit_amount])
        print 'You have deposited $',deposit_amount, ' into your account. You now have $',balance, ' Thank you.'
        return choice()
        break
#view balance chosen shows current balance#
    while action == '3':
        print 'Your current balance is $',balance, '. Thank you.'
        return choice()
        break
#view transactions chosen shows stored from this run previous transactions#
    while action == '4':
        for trans in transactions:
            print str(transactions)[1:-1]
            break
        return choice()
        break
#user chooses to exit the program#
    while action == '5':
        print 'Thank you and Goodbye.'
        break
    while action > '5':
        print 'Please enter a number 1 - 5.'
        return choice()
        break



greeting()
welcome()
choice()


