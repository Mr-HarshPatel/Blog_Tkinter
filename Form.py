from tkinter import *
from tkinter import messagebox
screen = Tk()
screen.title("Registration Form")
screen.geometry("400x400")
screen.resizable(False,False)

def register():
    name = str(name_info.get())
    age = str(age_info.get())
    phone = str(phone_info.get())
    email = str(email_info.get())

    if name=="" :
        messagebox.showerror("Error","Please Enter Your Name")
    elif age=="" :
        messagebox.showerror("Error", "Please Enter Your Age")
    elif phone=="" :
        messagebox.showerror("Error", "Please Enter Your Phone Number")
    elif email=="" :
        messagebox.showerror("Error", "Please Enter Your Email")
    else :
        Label(screen,text="Registration Successful",font="28",fg="green").place(x=135,y=285)
def clear():
    pass

label = Label(screen,text="Registration Form",font="arial 20 bold",bg="black",fg="white").pack(fill="both")
label = Label(screen,text="Name",font="20").place(x=40,y=75)
label = Label(screen,text="Age",font="20").place(x=40,y=115)
label = Label(screen,text="Phone No.",font="20").place(x=40,y=155)
label = Label(screen,text="Email Id",font="20").place(x=40,y=195)

name_info=StringVar
age_info=StringVar
phone_info=StringVar
email_info=StringVar
name_entry = Entry(screen,font="10",bd=4,textvariable=name_info)
name_entry.place(x=140,y=75)
age_entry = Entry(screen,font="10",bd=4,textvariable=age_info)
age_entry.place(x=140,y=115)
phone_entry = Entry(screen,font="10",bd=4,textvariable=phone_info)
phone_entry.place(x=140,y=155)
email_entry = Entry(screen,font="10",bd=4,textvariable=email_info)
email_entry.place(x=140,y=195)

button = Button(screen,text="Register",font="20",command=register)
button.place(x=185,y=255)
clear = Button(screen,text="Clear",font="20",command= clear)
clear.place(x=262,y=255)
mainloop()
