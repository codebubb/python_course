balance = 1000

def deposit():
    return int(raw_input("How much do you want to deposit?"))

# Main program
while True:

    print "Menu..."
    print "1) Deposit"
    print "2) Display balance"

    option = raw_input("Enter your option:")
    if option == "1":
        balance += deposit()
    if option == "2":
        print balance
