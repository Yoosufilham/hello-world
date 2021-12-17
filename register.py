from tkinter import *
root = Tk()
#root.geometry('500×300')

def getvals():
	print("User Loged in")

Label(root, text="LOGIN PAGE", font="ar 13 bold").grid(row=0, column=3)

u_name = Label(root, text="User Name")
email = Label(root, text="Email")
password = Label(root, text="Password")

u_name.grid(row=1, column=2)
email.grid(row=2, column=2)
password.grid(row=3, column=2)

u_namevalue = StringVar
emailvalue = StringVar
passwordvalue = StringVar
checkvalue = IntVar

u_nameentry = Entry(root, textvariable =u_namevalue)
emailentry = Entry(root, textvariable =passwordvalue)
passwordentry = Entry(root, textvariable =passwordvalue)

u_nameentry.grid(row=1, column=3)
emailentry.grid(row=2, column=3)
passwordentry.grid(row=3, column=3)

checkbtn = Checkbutton(text="remember me", variable = checkvalue)
checkbtn.grid(row=6, column= 3)

Button(text="Login", command=getvals).grid(row=7, column=3)




root.mainloop()
