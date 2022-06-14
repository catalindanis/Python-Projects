from tkinter import *
import threading
from Declarations import *

def PlayGame():
    player1 = player1Name.get()
    player2 = player2Name.get()

    if len(player1) > 0 and len(player2) > 0:
        text1.place_forget()
        text2.place_forget()
        player1Name.place_forget()
        player2Name.place_forget()
        playButton.place_forget()
        emptyName.place_forget()
        gameRunning()
    else:
        emptyName.place(x=135,y=280)

def win(winner):
    if(winner == 'X'):
        text = player1Name.get() + " WON!"
        global score_x
        score_x = score_x +1
    else:
        text = player2Name.get() + " WON!"
        global score_o
        score_o = score_o + 1
    winnerLabel.config(text=text,bg='red',fg='yellow',font=('arial',15))
    winnerLabel.place(x=25,y=370)
    timer = threading.Timer(1,reset)
    timer.start()
    PlayGame()

def checkGame():
    '''
    X O O
    O X 0
    0 O X
    '''
    if values[0][0] == values[0][1] == values[0][2]:#firs line
        win(values[0][0])
    elif values[1][0] == values[1][1] == values[1][2]:#second line
        win(values[1][0])
    elif values[2][0] == values[2][1] == values[2][2]:#third line
        win(values[2][0])
    elif values[0][0] == values[1][0] == values[2][0]:#first column
        win(values[0][0])
    elif values[0][1] == values[1][1] == values[2][1]:#second column
        win(values[0][1])
    elif values[0][2] == values[1][2] == values[2][2]:#third column
        win(values[0][2])
    elif values[0][0] == values[1][1] == values[2][2]:#first diagonal
        win(values[0][0])
    elif values[0][2] == values[1][1] == values[2][0]:#second diagonal
        win(values[0][2])

def reset():
    k = 0
    for i in range(0,3):
        for j in range(0,3):
            values[i][j] = k
            k=k+1
    print("DACA VEZI CONSOLA MA SUGI")
    top_left.config(text="")
    top_mid.config(text="")
    top_right.config(text="")
    mid_left.config(text="")
    mid_mid.config(text="")
    mid_right.config(text="")
    bottom_left.config(text="")
    bottom_mid.config(text="")
    bottom_right.config(text="")

def buttonPress(buttonName,button_index):
    global move
    correctMove = TRUE
    if buttonName.cget('text') == 'X' or buttonName.cget('text') == 'O':
        correctMove = FALSE;

    if(correctMove):
        if button_index == 1:
            values[0][0] = move
        elif button_index == 2:
            values[0][1] = move
        elif button_index == 3:
            values[0][2] = move
        elif button_index == 4:
            values[1][0] = move
        elif button_index == 5:
            values[1][1] = move
        elif button_index == 6:
            values[1][2] = move
        elif button_index == 7:
            values[2][0] = move
        elif button_index == 8:
            values[2][1] = move
        elif button_index == 9:
            values[2][2] = move
        buttonName.config(text=move,font=('Calibri',10),fg='black')
        if move == 'X': move = 'O'
        else: move = 'X'
        wrongMove.place_forget()
    else:
        wrongMove.place(x=38,y=375)

    checkGame()



def gameRunning():
    top_left.config(width=10,height=5,bg='gray',activebackground='gray',command=lambda:buttonPress(top_left,1))
    top_left.place(x=38,y=25)
    top_mid.config(width=10, height=5, bg='gray', activebackground='gray',command=lambda:buttonPress(top_mid,2))
    top_mid.place(x=162, y=25)
    top_right.config(width=10, height=5, bg='gray', activebackground='gray',command=lambda:buttonPress(top_right,3))
    top_right.place(x=287, y=25)
    mid_left.config(width=10, height=5, bg='gray', activebackground='gray',command=lambda:buttonPress(mid_left,4))
    mid_left.place(x=38, y=150)
    mid_mid.config(width=10, height=5, bg='gray', activebackground='gray',command=lambda:buttonPress(mid_mid,5))
    mid_mid.place(x=162, y=150)
    mid_right.config(width=10, height=5, bg='gray', activebackground='gray',command=lambda:buttonPress(mid_right,6))
    mid_right.place(x=287, y=150)
    bottom_left.config(width=10, height=5, bg='gray', activebackground='gray',command=lambda:buttonPress(bottom_left,7))
    bottom_left.place(x=38, y=275)
    bottom_mid.config(width=10, height=5, bg='gray', activebackground='gray',command=lambda:buttonPress(bottom_mid,8))
    bottom_mid.place(x=162, y=275)
    bottom_right.config(width=10, height=5, bg='gray', activebackground='gray',command=lambda:buttonPress(bottom_right,9))
    bottom_right.place(x=287, y=275)
    score.config(fg='white',text="SCORE: "+str(score_x)+":"+str(score_o),bg='black')
    score.place(x=320,y=370)


def runApp():
    game.geometry('400x400')
    game.title("TicTacToe")
    game.config(bg='black')

    text1.config(font=('calibri',10),bg='black',fg='white',text='Player1 Name (X):')
    text1.place(x=142,y=125)
    player1Name.config(bg='gray')
    player1Name.place(x=142,y=150)

    text2.config(font=('calibri',10),bg='black',fg='white',text='Player2 Name (O):')
    text2.place(x=142,y=175)
    player2Name.config(bg='gray')
    player2Name.place(x=142,y=200)

    playButton.config(text='PLAY',height=2,width=20,bg='darkred',fg='orange',command=PlayGame,activebackground='darkred')
    playButton.place(x=130,y=240)

    emptyName.config(bg='black', fg='red', text='Please Enter Your Names!')

    game.mainloop()

if __name__ == '__main__':
    runApp()



