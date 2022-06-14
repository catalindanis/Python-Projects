from tkinter import *
import string

game = Tk()
text1 = Label(game)
player1Name = Entry(game)
text2 = Label(game)
player2Name = Entry(game)
playButton = Button(game)
emptyName = Label(game)

player1 = StringVar()
player2 = StringVar()

top_left = Button(game)
top_mid = Button(game)
top_right = Button(game)
mid_left = Button(game)
mid_mid = Button(game)
mid_right = Button(game)
bottom_left = Button(game)
bottom_mid = Button(game)
bottom_right = Button(game)

score = Label(game)
winnerLabel = Label(game)
score_x=0
score_o=0

values = [[0,1,2],[3,4,5],[6,7,8]]
move = 'X'
wrongMove = Label(game)
wrongMove.config(text="Wrong Move", fg='red', bg='black', font='calibri')







