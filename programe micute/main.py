from tkinter import *

root = Tk()
root.geometry("300x150")

frame = Frame(root)
frame.pack()

text = Label(frame,text='Salut')
text.pack()

root.mainloop()