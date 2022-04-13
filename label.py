from tkinter import *
window = Tk()
window.title("Label in Tkinter")
# photo = PhotoImage(file="image.png")
label = Label(window,
              text = "Hello world",
              font=('Arial',40,'bold'),
              bg="black",
              fg="lightgreen",
              bd= 10,
              padx=10,
              pady=20,
              # image=photo,
              compound='bottom')
label.pack()
# label.place(x=0,y=0)
window.mainloop()