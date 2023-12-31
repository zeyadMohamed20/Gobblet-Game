import tkinter as tk
from PIL import Image, ImageTk
import os



app = None

class BoardWindow(object):
    player1 = None
    player2 = None
    turn = None
    def __init__(self, root, player1, player2, difficulty1=1, difficulty2=1, mode="AI VS AI"):
        self.trans = ImageTk.PhotoImage(file=os.getcwd()+"\\frame0\\trans.png", width=4, height=4)
        self.counter = 0
        self.difficulty1 = difficulty1
        self.difficulty2 = difficulty2
        self.stack_flag = None
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.turn = player1
        self.mode = mode
        self.current_player = Player.White
        self.root = root
        self.root.title("Gameplay")
        self.root.geometry("1200x650")
        self.root.resizable(False, False) 
        self.root.iconbitmap("./frame0/icon.ico")
        