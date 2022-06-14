from tkinter import *

def send():
    message_list.insert(INSERT,message_field.get()+'\n')

app = Tk()
app.geometry("300x300")
app.title("iMessage")

chat_frame = Frame(app)
chat_frame.pack(side=BOTTOM)

message_field = Entry(width=25,font=("calibri",15))
message_field.pack(in_=chat_frame,side='bottom')

pixel = PhotoImage(width=1,height=1)

button = Button(image=pixel,compound='c',width=25,height=25,text="SEND",command=send)
button.place(x=260,y=270)

message_list = Text(chat_frame,width=50,height=50)
message_list.pack(side='top')

app.resizable(width=FALSE,height=FALSE)
app.mainloop()

