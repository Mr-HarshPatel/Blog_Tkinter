from tkinter import *
def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You don't agree :(")
window = Tk()
window.title("CheckBox")
x = IntVar()
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           compound='left')
check_button.pack()
window.mainloop()