from Tkinter import *

def handle_submit(event):
    print "You entered: ", input_1.get()

root = Tk()
password_box = Label(root, text="Please enter your password")
input_1 = Entry(root, bd=5, show="*")
submit = Button(root, text ="Submit")
submit.bind("<Button-1>", handle_submit)
password_box.pack()
input_1.pack()
submit.pack(side=BOTTOM)
root.mainloop()
