import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import messagebox
from cell import *
import os
from Board import *
from Algo import *
import time


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
        
        # Player 0 Gobblet Stacks area
        self.player0_image = []
        self.player0_image.append(ImageTk.PhotoImage(file=os.getcwd()+"\\frame0\\circle-90.png", width=4, height=4))
        self.player0_image.append(ImageTk.PhotoImage(file=os.getcwd()+"\\frame0\\circle-70.png", width=4, height=4))
        self.player0_image.append(ImageTk.PhotoImage(file=os.getcwd()+"\\frame0\\circle-50.png", width=4, height=4))
        self.player0_image.append(ImageTk.PhotoImage(file=os.getcwd()+"\\frame0\\circle-30.png", width=4, height=4))
        self.player0_stack_image = [0,0,0]
        self.player0stack0 = tk.Button(self.bottom_frame, 
                                               bg="#B9A180", 
                                               activebackground="#A1662F",
                                               disabledforeground="red",
                                               bd=1, 
                                               cursor="hand1", 
                                               command=lambda: self.stack_click(Player.White, 0),
                                               relief="sunken", width=60, height=75, image = self.player0_image[0])
        self.player0stack0.place(x = 100, y = 450, width=100, height=100)

        self.player0stack1 = tk.Button(self.bottom_frame, 
                                               bg="#B9A180", 
                                               activebackground="#A1662F",
                                               disabledforeground="red",
                                               bd=1, 
                                               cursor="hand1", 
                                               command=lambda: self.stack_click(Player.White, 1),
                                               relief="sunken", width=60, height=75, image = self.player0_image[0])
        self.player0stack1.place(x = 100, y = 330, width=100, height=100)

        self.player0stack2 = tk.Button(self.bottom_frame, 
                                               bg="#B9A180", 
                                               activebackground="#A1662F",
                                               disabledforeground="red",
                                               bd=1, 
                                               cursor="hand1",  
                                               command=lambda: self.stack_click(Player.White, 2),
                                               relief="sunken", width=60, height=75, image = self.player0_image[0])
        self.player0stack2.place(x = 100, y = 210, width=100, height=100)

        self.player0_stacks = [self.player0stack0,self.player0stack1,self.player0stack2]
        self.player0_label = tk.Label(self.bottom_frame,text=f"Player 1\n{self.player1}",font=("Supply Center", 14), bg="#B9A180")
        self.player0_label.place(x = 110, y = 130)

        # Player 1 Gobblet Stacks area
        self.player1_image = []
        self.player1_image.append(ImageTk.PhotoImage(file=os.getcwd()+"\\frame0\\black-90.png", width=4, height=4))
        self.player1_image.append(ImageTk.PhotoImage(file=os.getcwd()+"\\frame0\\black-70.png", width=4, height=4))
        self.player1_image.append(ImageTk.PhotoImage(file=os.getcwd()+"\\frame0\\black-50.png", width=4, height=4))
        self.player1_image.append(ImageTk.PhotoImage(file=os.getcwd()+"\\frame0\\black-30.png", width=4, height=4))
        self.player1_stack_image = [0,0,0]
        self.player1stack0 = tk.Button(self.bottom_frame, 
                                               bg="#B9A180", 
                                               activebackground="#A1662F",
                                               disabledforeground="red",
                                               bd=1, 
                                               cursor="hand1",  
                                               command=lambda: self.stack_click(Player.Black, 0),
                                               relief="sunken", width=60, height=75, image = self.player1_image[0], 
                                               state="disabled")
        self.player1stack0.place(x = 1000, y = 50, width=100, height=100)

        self.player1stack1 = tk.Button(self.bottom_frame, 
                                               bg="#B9A180", 
                                               activebackground="#A1662F",
                                               disabledforeground="red",
                                               bd=1, 
                                               cursor="hand1",  
                                               command=lambda: self.stack_click(Player.Black, 1),
                                               relief="sunken", width=60, height=75, image = self.player1_image[0], 
                                               state="disabled")
        self.player1stack1.place(x = 1000, y = 170, width=100, height=100)

        self.player1stack2 = tk.Button(self.bottom_frame, 
                                               bg="#B9A180", 
                                               activebackground="#A1662F",
                                               disabledforeground="red",
                                               bd=1, 
                                               cursor="hand1", 
                                               command=lambda: self.stack_click(Player.Black, 2),
                                               relief="sunken", width=60, height=75, image = self.player1_image[0], 
                                               state="disabled")
        self.player1stack2.place(x = 1000, y = 290, width=100, height=100)
        # Bind the play_click_sound function to the mouse click event for the main window
        self.root.bind("<Button-1>", lambda event: play_click_sound())
        self.player1_stacks = [self.player1stack0,self.player1stack1,self.player1stack2]
        self.player1_label = tk.Label(self.bottom_frame,text=f"Player 2\n{self.player2}",font=("Supply Center", 14), bg="#B9A180")
        self.player1_label.place(x = 1010, y = 420)
        if self.mode == "AI VS AI":
            for btn in self.player0_stacks:
                btn['state'] = "disabled"

    def AIvsAI(self):
        if self.mode == "AI VS AI":
            self.turn_label = tk.Label(self.top_frame, text=f"Turn: {self.turn}", font=("Supply Center", 14), bg="#997950")
            self.turn_label.place(x=550, y = 5)
            time.sleep(2)
            for btn in self.player1_stacks:
                if btn != None:
                    btn['state'] = "disabled"
            for btn in self.player0_stacks:
                if btn != None:
                    btn['state'] = "disabled"
            for row in self.board_grid:
                for btn in row:
                    btn['state'] = "disabled"
            state = self.board.check_winner()
            Board.flag = False
            while(state == Player.NONE):
                self.root.update()
                time.sleep(2)
                temp = bot_turn(self.board, self.difficulty1, Player.White)
                self.board = copy.deepcopy(temp)
                if self.board.flag_add == True:
                    self.board_grid[self.board.curr_row][self.board.curr_col]['image'] = self.player0_image[self.player0_stack_image[self.board.curr_stack]]
                    self.player0_stack_image[self.board.curr_stack] += 1
                    if self.player0_stack_image[self.board.curr_stack] >= 4:
                        self.player0_stacks[self.board.curr_stack].destroy()
                        self.player0_stacks[self.board.curr_stack] = None
                    else:
                        self.player0_stacks[self.board.curr_stack]['image'] = self.player0_image[self.player0_stack_image[self.board.curr_stack]]
                else:
                    prevCell_owner,prevCell_size = self.board.board_cells[self.board.from_row][self.board.from_col].get_gobblet()
                    currCell_owner,currCell_size = self.board.board_cells[self.board.to_row][self.board.to_col].get_gobblet()
                    if prevCell_size == 8:
                        prev_index = 0
                    elif prevCell_size == 4:
                        prev_index = 1
                    elif prevCell_size == 2:
                        prev_index = 2
                    elif prevCell_size == 1:
                        prev_index = 3
                    else: prev_index = None

                    if currCell_size == 8:
                        curr_index = 0
                    elif currCell_size == 4:
                        curr_index = 1
                    elif currCell_size == 2:
                        curr_index = 2
                    elif currCell_size == 1:
                        curr_index = 3
                    else: curr_index = None

                    if(prevCell_owner == Player.White):
                        if prev_index != None:
                            self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.player0_image[prev_index]
                        else:
                            self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.trans
                    else:
                        if prev_index != None:
                            self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.player1_image[prev_index]
                        else:
                            self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.trans

                    if(currCell_owner == Player.White):
                        self.board_grid[self.board.to_row][self.board.to_col]['image'] = self.player0_image[curr_index]
                    else:
                        self.board_grid[self.board.to_row][self.board.to_col]['image'] = self.player1_image[curr_index]
                        

                self.current_player = Player.Black
                self.turn_label['text'] = f"Turn: {self.player2}"
                self.root.update()
                time.sleep(2)
                self.state = self.board.check_winner()
                if(self.state != Player.NONE):
                    break
                temp = bot_turn(self.board, self.difficulty2, Player.Black)
                self.board = copy.deepcopy(temp)
                if self.board.flag_add == True:
                    self.board_grid[self.board.curr_row][self.board.curr_col]['image'] = self.player1_image[self.player1_stack_image[self.board.curr_stack]]
                    self.player1_stack_image[self.board.curr_stack] += 1
                    if self.player1_stack_image[self.board.curr_stack] >= 4:
                        self.player1_stacks[self.board.curr_stack].destroy()
                        self.player1_stacks[self.board.curr_stack] = None
                    else:
                        self.player1_stacks[self.board.curr_stack]['image'] = self.player1_image[self.player1_stack_image[self.board.curr_stack]]
                else:
                    prevCell_owner,prevCell_size = self.board.board_cells[self.board.from_row][self.board.from_col].get_gobblet()
                    currCell_owner,currCell_size = self.board.board_cells[self.board.to_row][self.board.to_col].get_gobblet()
                    if prevCell_size == 8:
                        prev_index = 0
                    elif prevCell_size == 4:
                        prev_index = 1
                    elif prevCell_size == 2:
                        prev_index = 2
                    elif prevCell_size == 1:
                        prev_index = 3
                    else: prev_index = None

                    if currCell_size == 8:
                        curr_index = 0
                    elif currCell_size == 4:
                        curr_index = 1
                    elif currCell_size == 2:
                        curr_index = 2
                    elif currCell_size == 1:
                        curr_index = 3
                    else: curr_index = None

                    if(prevCell_owner == Player.White):
                        if prev_index != None:
                            self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.player0_image[prev_index]
                        else:
                            self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.trans
                    else:
                        if prev_index != None:
                            self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.player1_image[prev_index]
                        else:
                            self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.trans

                    if(currCell_owner == Player.White):
                        self.board_grid[self.board.to_row][self.board.to_col]['image'] = self.player0_image[curr_index]
                    else:
                        self.board_grid[self.board.to_row][self.board.to_col]['image'] = self.player1_image[curr_index]
                self.current_player = Player.White
                self.turn_label['text'] = f"Turn: {self.player1}"
                self.current_stack = None
                self.stack_flag = False
                self.state = self.board.check_winner()
            
            p = None
            if self.state == Player.Black:
                p = f"{self.player2} - Player 2"
            else:
                p = f"{self.player1} - Player 1"
            result = messagebox.askquestion("Winner Winner", f"There is a Winner!\nCongratulation, {p}\nDo you want a rematch?", icon='info', )
            if result == 'no':
                self.root.destroy()
            else:
                # Destroy all child widgets in the main window
                for widget in self.root.winfo_children():
                    widget.destroy()
                start(self.root, self.player1, self.player2, 3, self.difficulty1, self.difficulty2)

    def stack_click(self, player, stack):
        self.stack_flag = True
        if player == Player.White:
            self.current_stack = stack
            self.current_player = Player.White
            for btn in self.player0_stacks:
                if btn != None:
                    btn['state'] = "disabled"
        else:
            self.current_stack = stack
            self.current_player = Player.Black
            for btn in self.player1_stacks:
                if btn != None:
                    btn['state'] = "disabled"
    
    def grid_click(self, row, col):
        if self.stack_flag == True:
            if self.current_player == Player.White:
                if self.board.player_add_gobblet(row, col, Player.White, (8>>(self.player0_stack_image[self.current_stack])) ,self.current_stack):
                    self.board_grid[row][col]['image'] = self.player0_image[self.player0_stack_image[self.current_stack]]
                    self.player0_stack_image[self.current_stack] += 1
                    if self.player0_stack_image[self.current_stack] >= 4:
                        self.player0_stacks[self.current_stack].destroy()
                        self.player0_stacks[self.current_stack] = None
                    else:
                        self.player0_stacks[self.current_stack]['image'] = self.player0_image[self.player0_stack_image[self.current_stack]]
                for btn in self.player1_stacks:
                    if btn != None:
                        btn['state'] = "normal"
                self.board.play_next()
                self.current_player = Player.Black
                self.turn_label['text'] = f"Turn: Player 2 - {self.player2}"
                self.root.update()
                if self.mode == "Player VS AI":
                    Board.flag = True
                    temp = bot_turn(self.board, self.difficulty1, Player.Black)
                    self.board = copy.deepcopy(temp)
                    if self.board.flag_add == True:
                        self.board_grid[self.board.curr_row][self.board.curr_col]['image'] = self.player1_image[self.player1_stack_image[self.board.curr_stack]]
                        self.player1_stack_image[self.board.curr_stack] += 1
                        if self.player1_stack_image[self.board.curr_stack] >= 4:
                            self.player1_stacks[self.board.curr_stack].destroy()
                            self.player1_stacks[self.board.curr_stack] = None
                        else:
                            self.player1_stacks[self.board.curr_stack]['image'] = self.player1_image[self.player1_stack_image[self.board.curr_stack]]
                    else:
                        prevCell_owner,prevCell_size = self.board.board_cells[self.board.from_row][self.board.from_col].get_gobblet()
                        currCell_owner,currCell_size = self.board.board_cells[self.board.to_row][self.board.to_col].get_gobblet()
                        if prevCell_size == 8:
                            prev_index = 0
                        elif prevCell_size == 4:
                            prev_index = 1
                        elif prevCell_size == 2:
                            prev_index = 2
                        elif prevCell_size == 1:
                            prev_index = 3
                        else: prev_index = None

                        if currCell_size == 8:
                            curr_index = 0
                        elif currCell_size == 4:
                            curr_index = 1
                        elif currCell_size == 2:
                            curr_index = 2
                        elif currCell_size == 1:
                            curr_index = 3
                        else: curr_index = None

                        if(prevCell_owner == Player.White):
                            if prev_index != None:
                                self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.player0_image[prev_index]
                            else:
                                self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.trans
                        else:
                            if prev_index != None:
                                self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.player1_image[prev_index]
                            else:
                                self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.trans

                        if(currCell_owner == Player.White):
                            self.board_grid[self.board.to_row][self.board.to_col]['image'] = self.player0_image[curr_index]
                        else:
                            self.board_grid[self.board.to_row][self.board.to_col]['image'] = self.player1_image[curr_index]

                    for btn in self.player1_stacks:
                        if btn != None:
                            btn['state'] = "disabled"
                    for btn in self.player0_stacks:
                        if btn != None:
                            btn['state'] = "normal"
                    self.current_player = Player.White
                    self.turn_label['text'] = f"Turn: Player 2 - {self.player1}"
                    self.current_stack = None
                    self.stack_flag = False

            else:
                if self.board.player_add_gobblet(row, col, Player.Black, (8>>(self.player1_stack_image[self.current_stack])) ,self.current_stack):
                    self.board.play_next()
                    self.board_grid[row][col]['image'] = self.player1_image[self.player1_stack_image[self.current_stack]]
                    self.player1_stack_image[self.current_stack] += 1
                    if self.player1_stack_image[self.current_stack] >= 4:
                        self.player1_stacks[self.current_stack].destroy()
                        self.player1_stacks[self.current_stack] = None
                    else:
                        self.player1_stacks[self.current_stack]['image'] = self.player1_image[self.player1_stack_image[self.current_stack]]
                for btn in self.player0_stacks:
                    if btn != None:
                        btn['state'] = "normal"
                self.current_player = Player.White
                self.turn_label['text'] = f"Turn: Player 1 - {self.player1}"
            self.current_stack = None
            self.stack_flag = False
        else:
            if(self.counter == 0):
                curr, _ = self.board.board_cells[row][col].get_gobblet()
                if curr != self.current_player:
                    return
                for btn in self.player1_stacks:
                    if btn != None:
                        btn['state'] = "disabled"
                for btn in self.player0_stacks:
                    if btn != None:
                        btn['state'] = "disabled"
                self.counter += 1
                self.prev_row = row
                self.prev_col = col
            else:
                if self.prev_col == col and self.prev_row == row:
                    return
                self.counter = 0
                if self.board.move_gobblet(self.current_player, self.prev_row, self.prev_col, row, col):
                    self.board.play_next()
                    prevCell_owner,prevCell_size = self.board.board_cells[self.prev_row][self.prev_col].get_gobblet()
                    currCell_owner,currCell_size = self.board.board_cells[row][col].get_gobblet()
                    if prevCell_size == 8:
                        prev_index = 0
                    elif prevCell_size == 4:
                        prev_index = 1
                    elif prevCell_size == 2:
                        prev_index = 2
                    elif prevCell_size == 1:
                        prev_index = 3
                    else: prev_index = None

                    if currCell_size == 8:
                        curr_index = 0
                    elif currCell_size == 4:
                        curr_index = 1
                    elif currCell_size == 2:
                        curr_index = 2
                    elif currCell_size == 1:
                        curr_index = 3
                    else: curr_index = None
                    
                    if(prevCell_owner == Player.White):
                        if prev_index != None:
                            self.board_grid[self.prev_row][self.prev_col]['image'] = self.player0_image[prev_index]
                        else:
                            self.board_grid[self.prev_row][self.prev_col]['image'] = self.trans
                    else:
                        if prev_index != None:
                            self.board_grid[self.prev_row][self.prev_col]['image'] = self.player1_image[prev_index]
                        else:
                            self.board_grid[self.prev_row][self.prev_col]['image'] = self.trans

                    if(currCell_owner == Player.White):
                        self.board_grid[row][col]['image'] = self.player0_image[curr_index]
                    else:
                        self.board_grid[row][col]['image'] = self.player1_image[curr_index]

                if self.current_player == Player.Black:
                    self.current_player = Player.White
                    self.turn_label['text'] = f"Turn: Player 1 - {self.player1}"
                    for btn in self.player0_stacks:
                        if btn != None:
                            btn['state'] = "normal"
                else:
                    self.root.update()
                    self.current_player = Player.Black
                    self.turn_label['text'] = f"Turn: Player 2 - {self.player2}"
                    for btn in self.player1_stacks:
                        if btn != None:
                            btn['state'] = "normal"   
                    if self.mode == "Player VS AI":
                        temp = bot_turn(self.board, self.difficulty1, Player.Black)
                        self.board = copy.deepcopy(temp)
                        if self.board.flag_add == True:
                            self.board_grid[self.board.curr_row][self.board.curr_col]['image'] = self.player1_image[self.player1_stack_image[self.board.curr_stack]]
                            self.player1_stack_image[self.board.curr_stack] += 1
                            if self.player1_stack_image[self.board.curr_stack] >= 4:
                                self.player1_stacks[self.board.curr_stack].destroy()
                                self.player1_stacks[self.board.curr_stack] = None
                            else:
                                self.player1_stacks[self.board.curr_stack]['image'] = self.player1_image[self.player1_stack_image[self.board.curr_stack]]
                        else:
                            prevCell_owner,prevCell_size = self.board.board_cells[self.board.from_row][self.board.from_col].get_gobblet()
                            currCell_owner,currCell_size = self.board.board_cells[self.board.to_row][self.board.to_col].get_gobblet()
                            if prevCell_size == 8:
                                prev_index = 0
                            elif prevCell_size == 4:
                                prev_index = 1
                            elif prevCell_size == 2:
                                prev_index = 2
                            elif prevCell_size == 1:
                                prev_index = 3
                            else: prev_index = None

                            if currCell_size == 8:
                                curr_index = 0
                            elif currCell_size == 4:
                                curr_index = 1
                            elif currCell_size == 2:
                                curr_index = 2
                            elif currCell_size == 1:
                                curr_index = 3
                            else: curr_index = None

                            if(prevCell_owner == Player.White):
                                if prev_index != None:
                                    self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.player0_image[prev_index]
                                else:
                                    self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.trans
                            else:
                                if prev_index != None:
                                    self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.player1_image[prev_index]
                                else:
                                    self.board_grid[self.board.from_row][self.board.from_col]['image'] = self.trans

                            if(currCell_owner == Player.White):
                                self.board_grid[self.board.to_row][self.board.to_col]['image'] = self.player0_image[curr_index]
                            else:
                                self.board_grid[self.board.to_row][self.board.to_col]['image'] = self.player1_image[curr_index]

                        for btn in self.player1_stacks:
                            if btn != None:
                                btn['state'] = "disabled"
                        for btn in self.player0_stacks:
                            if btn != None:
                                btn['state'] = "normal"
                        self.current_player = Player.White
                        self.turn_label['text'] = f"Turn: Player 1 - {self.player1}"
                        self.current_stack = None
                        self.stack_flag = False

   
            
        temp = self.board.check_winner()
        p = None
        if temp != Player.NONE:
            if temp == Player.Black:
                p = f"{self.player2} - Player 2"
            else:
                p = f"{self.player1} - Player 1"
            result = messagebox.askquestion("Winner Winner", f"There is a Winner!\nCongratulation, {p}\nDo you want a rematch?", icon='info', )
            if result == 'no':
                self.root.destroy()
            else:
                # Destroy all child widgets in the main window
                for widget in self.root.winfo_children():
                    widget.destroy()
                if self.mode == "Player VS AI": mode = 2 
                else: mode = 1
                start(self.root, self.player1, self.player2, mode, self.difficulty1, self.difficulty2)
    
    def confirm_quit(self):
        result = messagebox.askquestion("Quit", "Are you sure you want to quit?", icon='warning')
        if result == 'yes':
            self.root.destroy()
         
    
def start(root, p1, p2,mode=1, d1=None, d2=None):
    global app
    if mode==1:
        msg = "Player VS Player"
    elif mode == 2:
        msg = "Player VS AI"
    elif mode == 3:
        msg = "AI VS AI"
    else:
        return
    app = BoardWindow(root, player1=p1, player2=p2, difficulty1=d1, difficulty2=d2, mode=msg)
    root.mainloop()