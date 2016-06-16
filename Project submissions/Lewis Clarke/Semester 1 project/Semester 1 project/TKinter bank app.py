from Tkinter import *
import Tkinter as tk
import tkMessageBox
import hashlib
import time
import os

global username
username = []

class App(Frame,object):
    ''' Main foundation for the GUI'''

    def __init__ (self, master):
        
        super(App,self).__init__(master)
        self.grid()
        self.create_widgets()
        balance = 0
        self.balance = balance
        
        

    def create_widgets(self):

        global log_var
        log_var = StringVar()
        global pass_var
        pass_var = StringVar()

        self.user_lbl = Label(self, text = 'User Name', bg = '#e2e2e2',font = ('LANE-NARROW', 12))
        self.user_ent = Entry(self, textvariable = log_var)
        self.user_lbl.grid(row = 2, column = 1)
        self.user_ent.grid(row = 2, column = 2)
        
        
        self.log_lbl = Label(self, text = 'Please Login To Continue:', bg = '#e2e2e2', font =('LANE-NARROW', 12))
        self.log_lbl.grid(row = 1, column = 2,)
        self.l_btn = Button(self, text = 'Login', font = ('LANE-NARROW',10), command = self.login_check) 
        self.l_btn.grid(row = 4,column = 2,padx = 5, pady = 5)

        

        self.pass_lbl = Label(self, text = 'Password', bg = '#e2e2e2', font = ('LANE-NARROW', 12))
        self.pass_ent = Entry(self, textvariable = pass_var)
        self.pass_lbl.grid(row = 3, column = 1)
        self.pass_ent.grid(row = 3, column = 2)


        self.ac_lbl = Label(self, text = 'Create A New Account:',bg = '#e2e2e2', font =('LANE-NARROW', 12))
        self.ac_btn = Button(self, text = 'Create account', font = ('LANE-NARROW',10),command = lambda : controller.show_frame(Main_page))
        self.ac_lbl.grid(row = 5, column = 1 )
        self.ac_btn.grid(row = 5,column = 2,padx = 5, pady = 5)

        self.configure(background = '#e2e2e2')


        photo = PhotoImage(file = 'Bank_logo.gif')
        p = Label(self,image = photo)
        p.image = photo
        p.grid(row = 0,columnspan = 4)


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
                    
                    
                        # This checks that the user input matched the username and password that was hashed to the main file
                        # if that input, once hased does not match that in the file then the user will not be able to log in
                else:
                    del username[0]
                            # if that happend once again the global variable list is cleared and the while loop is started again
                    tkMessageBox.showinfo('Error', 'Username or password Incorrect please try again')
                        



    

root = Tk()        
root.title('Banking App')
root.geometry('450x450')
root.wm_iconbitmap('favicon.ico')
bank = App(root)
root.mainloop()

