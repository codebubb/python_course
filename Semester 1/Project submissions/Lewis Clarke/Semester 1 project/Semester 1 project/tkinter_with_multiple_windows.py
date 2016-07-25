from Tkinter import *
import Tkinter as tk
import tkMessageBox
import hashlib
import time
import os


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
        print log_var.get()
        print pass_var.get()
            
        userid = log_var.get()
        username.append(userid)
      
        passid = pass_var.get()
                # when a user comes to log in there input is saved t the variable above and appened to the global variable username
        try:
            f = open(log_var.get() + '.txt', 'r')
                    # looks for the file with the users input plus the txt extention
        except IOError:
            tkMessageBox.showinfo('Error', 'Username Not Found')
            del username[0]
                # if that file is not found the global variable is deleted at index 0, in other words the list is cleared
                # to prevent the wrong input creating a completely new file once the correct input is entered.  
        finally:
            with f:
                x = f.readlines()
                user_input = hashlib.md5()
                user_input.update(userid)
                pass_input = hashlib.md5()
                pass_input.update(passid)
                if x[0] == user_input.hexdigest() + '\n' and x[1] == pass_input.hexdigest():
                    last_bal = open(log_var.get() + 'balance.txt', 'r')
                    lb = last_bal.readlines()
                    self.balance = int(''.join(lb[0]))
                    print self.balance
                    return bank.show_frame(Main_page)
                    
                        
                        # This checks that the user input matched the username and password that was hashed to the main file
                        # if that input, once hased does not match that in the file then the user will not be able to log in
                else:
                    del username[0]
                            # if that happend once again the global variable list is cleared and the while loop is started again
                    tkMessageBox.showinfo('Error', 'Username or password Incorrect please try again')
                        




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




    

class Bank_app(tk.Tk):

    def __init__ (self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self,'Banking App')
        tk.Tk.geometry(self,'450x450')
        tk.Tk.wm_iconbitmap(self,'favicon.ico')
        
        container = tk.Frame(self)

        container.pack(side = 'top', fill = 'both', expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (Startpage,Main_page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame(Startpage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Startpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        global log_var
        log_var = StringVar()
        global pass_var
        pass_var = StringVar()

        user_lbl = tk.Label(self, text = 'User Name', bg = '#e2e2e2',font = ('LANE-NARROW', 12))
        user_ent = tk.Entry(self, textvariable = log_var)
        user_lbl.grid(row = 2, column = 1)
        user_ent.grid(row = 2, column = 2)
        
        
        log_lbl = tk.Label(self, text = 'Please Login To Continue:', bg = '#e2e2e2', font =('LANE-NARROW', 12))
        log_lbl.grid(row = 1, column = 2,)
        l_btn = tk.Button(self, text = 'Login', font = ('LANE-NARROW',10),command = cust.login_check) 
        l_btn.grid(row = 4,column = 2,padx = 5, pady = 5)

        

        pass_lbl = tk.Label(self, text = 'Password', bg = '#e2e2e2', font = ('LANE-NARROW', 12))
        pass_ent = tk.Entry(self, textvariable = pass_var)
        pass_lbl.grid(row = 3, column = 1)
        pass_ent.grid(row = 3, column = 2)


        ac_lbl = tk.Label(self, text = 'Create A New Account:',bg = '#e2e2e2', font =('LANE-NARROW', 12))
        ac_btn = tk.Button(self, text = 'Create account', font = ('LANE-NARROW',10),command = lambda : controller.show_frame(Main_page))
        ac_lbl.grid(row = 5, column = 1 )
        ac_btn.grid(row = 5,column = 2,padx = 5, pady = 5)

        self.configure(background = '#e2e2e2')


        photo = PhotoImage(file = 'Bank_logo.gif')
        p = Label(self,image = photo)
        p.image = photo
        p.grid(row = 0,columnspan = 4)


class Main_page(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
            
        user_lbl = tk.Label(self, text = 'User Name', bg = '#e2e2e2',font = ('LANE-NARROW', 12))
        user_ent = tk.Entry(self)
        user_lbl.grid(row = 2, column = 0)
        user_ent.grid(row = 2, column = 1)

        log_lbl = tk.Label(self, text = 'Please Login To Continue:', bg = '#e2e2e2', font =('LANE-NARROW', 10))
        log_lbl.grid(row = 0, column = 0,)
        
        pass_lbl = tk.Label(self, text = 'Password', bg = '#e2e2e2', font = ('LANE-NARROW', 12))
        pass_ent = tk.Entry(self)
        pass_lbl.grid(row = 3, column = 0)
        pass_ent.grid(row = 3, column = 1)


        ac_lbl = tk.Label(self, text = 'This is page 2:',bg = '#e2e2e2', font =('LANE-NARROW', 12))
        ac_btn = tk.Button(self, text = 'Create account', font = ('LANE-NARROW',10),command = lambda : controller.show_frame(Startpage))
        ac_lbl.grid(row = 5, column = 0 )
        ac_btn.grid(row = 5,column = 0,padx = 5, pady = 5)

        self.configure(background = '#e2e2e2')

        


        photo = PhotoImage(file = 'Bank_logo_main.gif')
        p = Label(self,image = photo)
        p.image = photo
        p.grid(row = 0,column = 1)



cust = Bank_account()
new_cust = Overdraft()
bank = Bank_app()        
bank.mainloop()


  
        
