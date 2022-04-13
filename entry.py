from tkinter import *
def submit():
    username = entry.get()
    print(username)


window = Tk()
window.title("Entry Widget")
entry = Entry(window,
              font=("Arial",50),
              fg="yellow",
              bg="black")
entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)
window.mainloop()
