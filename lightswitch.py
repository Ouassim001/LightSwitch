from tkinter import *

toggle = Tk()

toggle.title("Theme Toggle")

toggle.geometry("400x500")

def black():
    toggle.config(bg="#000000")

def white():
    toggle.config(bg="#ffffff")



btn1 = Button(toggle, text="black",command=black)
btn1.pack()

btn2 = Button(toggle, text="white",command=white)
btn2.pack()






toggle.mainloop()