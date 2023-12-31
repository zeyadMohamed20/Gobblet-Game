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
        
        # Part 1: Top part
        self.top_frame = tk.Frame(self.root, height=40, bg="#997950")
        self.top_frame.pack(fill=tk.X)

        # Mode label
        self.modelabel = tk.Label(self.top_frame, text=f"Mode: {self.mode}", font=("Supply Center", 14), bg="#997950")
        self.modelabel.place(x=10, y = 5)

        # Turn label
        self.turn_label = tk.Label(self.top_frame, text=f"Turn: Player 1 - {self.turn}", font=("Supply Center", 14), bg="#997950")
        
        if self.mode == "AI VS AI":
            self.turn_label = tk.Button(self.top_frame, text="START",font=("Supply Center", 14), bg="#997950",activebackground="#795C32", bd=0, cursor="hand2", command=self.AIvsAI)
        self.turn_label.place(x=550, y = 5)

        # Quit button
        self.quit_button = tk.Button(self.top_frame, text="Quit",font=("Supply Center", 14),bg="#997950", bd=0,activebackground="#660000", cursor="hand2", command=self.confirm_quit)
        self.quit_button.place(x=1130, y = 4)