from tkinter import *
from pytube import YouTube
from tkinter import filedialog

def download(link):
    error_text = Label(text="INVALID FORMAT",fg='red',bg='gray',font=('arial',10))
    try:
        url = YouTube(link)
        stream = url.streams.get_highest_resolution()
        location = filedialog.askdirectory()
        stream.download(location)
        error_text.config(text="DOWNLOAD SUCCEEDED",fg='yellow')
        error_text.place(x=70,y=100)
    except:
        error_text.place(x=100,y=100)



def runApp():
    app = Tk()
    app.geometry("300x300")
    app.title("Youtube Downloader")
    app.config(bg='gray')

    text = Label(app,text="Made By Danis")
    text.config(font=("calibri",10),bg='gray',fg='black')
    text.place(x=210,y=280)

    link_field = Entry(app)
    link_field.config(width=50,bg='darkgray')
    link_field.place(y=25)

    text1 = Label(app,text = "Enter your link below: ")
    text1.config(font=("arial",13),bg='gray',fg='black')
    text1.pack()

    pixel = PhotoImage(width=1,height=1)
    download_button = Button(app,image=pixel)
    download_button.config(width=100,height=30,bg='darkgray',text='Download',font=("arial",15),compound='c',
                         command=lambda:download(link_field.get()))
    download_button.place(x=100,y=50)

    app.mainloop()

if __name__ == '__main__':
    runApp()