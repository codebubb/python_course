from Tkinter import *

root = Tk()
attempts = 3
password_box = Label(root, text="Please enter your password \n you have 3 attempts left")
entry = Entry(root, bd=5)

def password():
    if password == "password123":
        print ("Your password is correct")

submit = Button(root, text ="Submit", command = password)

password_box.pack()
entry.pack()
submit.pack(side=BOTTOM)
root.mainloop()
