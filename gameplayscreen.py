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
        
        # Part 2: Bottom part
        self.bottom_frame = tk.Frame(self.root, bg="#B9A180")
        self.bottom_frame.pack(fill=tk.BOTH, expand=True)

        # grid 4*4
        self.TableCell00 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2", 
                                               command = lambda: self.grid_click(0,0),
                                               relief="solid", width=120, height=130)
        self.TableCell00.place(x = 350, y = 20, width=120, height=130)

        self.TableCell01 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(0,1),
                                               relief="solid", width=120, height=130)
        self.TableCell01.place(x = 480, y = 20, width=120, height=130)

        self.TableCell02 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(0,2),
                                               relief="solid", width=120, height=130)
        self.TableCell02.place(x = 610, y = 20, width=120, height=130)

        self.TableCell03 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(0,3),
                                               relief="solid", width=120, height=130)
        self.TableCell03.place(x = 740, y = 20, width=120, height=130)


        self.TableCell10 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2", 
                                               command = lambda: self.grid_click(1,0),
                                               relief="solid", width=120, height=130)
        self.TableCell10.place(x = 350, y = 160, width=120, height=130)

        self.TableCell11 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(1,1),
                                               relief="solid", width=120, height=130)
        self.TableCell11.place(x = 480, y = 160, width=120, height=130)

        self.TableCell12 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(1,2),
                                               relief="solid", width=120, height=130)
        self.TableCell12.place(x = 610, y = 160, width=120, height=130)

        self.TableCell13 = tk.Button(self.bottom_frame, 
                                                bg="#A1662F", 
                                                activebackground="#770000",
                                                bd=1, 
                                                cursor="hand2",  
                                               command = lambda: self.grid_click(1,3),
                                                relief="solid", width=120, height=130)
        self.TableCell13.place(x = 740, y = 160, width=120, height=130)

        self.TableCell20 = tk.Button(self.bottom_frame, 
                                                bg="#A1662F", 
                                                activebackground="#770000",
                                                bd=1, 
                                                cursor="hand2",  
                                               command = lambda: self.grid_click(2,0),
                                                relief="solid", width=120, height=130)
        self.TableCell20.place(x = 350, y = 300, width=120, height=130)

        self.TableCell21 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(2,1),
                                               relief="solid", width=120, height=130)
        self.TableCell21.place(x = 480, y = 300, width=120, height=130)

        self.TableCell22 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(2,2),
                                               relief="solid", width=120, height=130)
        self.TableCell22.place(x = 610, y = 300, width=120, height=130)

        self.TableCell23 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(2,3),
                                               relief="solid", width=120, height=130)
        self.TableCell23.place(x = 740, y = 300, width=120, height=130)


        self.TableCell30 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2", 
                                               command = lambda: self.grid_click(3,0), 
                                               relief="solid", width=120, height=130)
        self.TableCell30.place(x = 350, y = 440, width=120, height=130)

        self.TableCell31 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(3,1),
                                               relief="solid", width=120, height=130)
        self.TableCell31.place(x = 480, y = 440, width=120, height=130)

        self.TableCell32 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(3,2),
                                               relief="solid", width=120, height=130)
        self.TableCell32.place(x = 610, y = 440, width=120, height=130)

        self.TableCell33 = tk.Button(self.bottom_frame, 
                                               bg="#A1662F", 
                                               activebackground="#770000",
                                               bd=1, 
                                               cursor="hand2",  
                                               command = lambda: self.grid_click(3,3),
                                               relief="solid", width=120, height=130)
        self.TableCell33.place(x = 740, y = 440, width=120, height=130)

        self.board_grid = [[self.TableCell00,self.TableCell01,self.TableCell02,self.TableCell03],
                           [self.TableCell10,self.TableCell11,self.TableCell12,self.TableCell13],
                           [self.TableCell20,self.TableCell21,self.TableCell22,self.TableCell23],
                           [self.TableCell30,self.TableCell31,self.TableCell32,self.TableCell33]]
        