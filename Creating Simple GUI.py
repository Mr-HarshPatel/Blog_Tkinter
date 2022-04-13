from tkinter import *


window = Tk() #instantiate an instance of a window

window.geometry("300x300")  # Setting the window size as width=600 and height=400
window.title("Our first GUI")  # Title of our GUI Screen.
icon = PhotoImage(file="image3.png")  #Passing image file for displaying icon.
window.iconphoto(True,icon)  #the iconphoto is builtin function which has two argument.

window.config(background="cyan")  #Or you can write hex color code:5c5cff

window.mainloop()  #place window on computer screen and listen # for evnets






















