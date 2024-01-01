import tkinter as tk
from tkinter import ttk
from controlFunctions import update_bot1_level, update_bot2_level
from gameplayScreen import *

start_window = None

def showStart(root, mode):
    update_bot1_level("Easy")
    update_bot2_level("Easy")
    # Create the start window
    global start_window
    start_window = tk.Toplevel(root)
    start_window.title("Start Game")
    start_window.iconbitmap("./frame0/icon.ico")
    start_window.configure(bg="#B9A180")
    
    start_window.resizable(False, False)
    player1_label = tk.Label(start_window, text="Player 1 Name", bg="#B9A180")
    player2_label = tk.Label(start_window, text="Player 2 Name", bg="#B9A180")
    player1_name = tk.Text(start_window, width=50, height=1)
    player2_name = tk.Text(start_window, width=50, height=1)

    ai_levels = ["Easy", "Medium", "Hard"]
    bot1level_label = tk.Label(start_window, text="Bot 1 Level", bg="#B9A180")
    bot2level_label = tk.Label(start_window, text="Bot 2 Level", bg="#B9A180")
    bot1_combobox = ttk.Combobox(start_window, values=ai_levels, state="readonly")
    bot1_combobox.set(update_bot1_level())  # Set initial value

    bot2_combobox = ttk.Combobox(start_window, values=ai_levels, state="readonly")
    bot2_combobox.set(update_bot2_level())  # Set initial value

    start_btn = tk.Button(start_window, text="Let's Gobble!", bd=1, cursor="hand2", relief="raised", bg="#997950", activebackground="#4B382A")

    # Function to update AI level when selected
    def on_combobox_selected1(event):
        selected_level = bot1_combobox.get()
        update_bot1_level(selected_level)

    # Function to update AI level when selected
    def on_combobox_selected2(event):
        selected_level = bot2_combobox.get()
        update_bot2_level(selected_level)

    # Bind the function to the Combobox selection event
    bot1_combobox.bind("<<ComboboxSelected>>", on_combobox_selected1)
    bot2_combobox.bind("<<ComboboxSelected>>", on_combobox_selected2)

    if mode == 1:
        width = 350
        height = 200
        start_window.geometry(f"{width}x{height}")
        player1_label.place(x=20, y=30)
        player1_name.place(x=120,y=30, width=200)
        player2_label.place(x=20, y=90)
        player2_name.place(x=120,y=90, width=200)
        start_btn['command'] = lambda: go(tk.Toplevel(root), player1_name.get(1.0, "end-1c"), player2_name.get(1.0, "end-1c"), None, None, 1)
        start_btn.place(x=130, y=140, width=100, height=40)
    elif mode == 2:
        width = 350
        height = 250
        start_window.geometry(f"{width}x{height}")
        player1_label.place(x=20, y=30)
        player1_name.place(x=120,y=30, width=200)
        player2_label.place(x=20, y=90)
        player2_name.insert(1.0, "Bot 1")
        player2_name['state'] = "disabled"
        player2_name.place(x=120,y=90, width=200)
        # add bot 1 level
        bot1level_label.place(x=20, y=140)
        bot1_combobox.place(x=120, y=140)   
        start_btn['command'] = lambda: go(tk.Toplevel(root), player1_name.get(1.0, "end-1c"), player2_name.get(1.0, "end-1c"), update_bot1_level(), None, 2)
        start_btn.place(x=130, y=180, width=100, height=40)
    elif mode == 3:
        width = 350
        height = 350
        start_window.geometry(f"{width}x{height}")
        player1_label.place(x=20, y=30)
        player1_name.insert(1.0, "Bot 1")
        player1_name['state'] = "disabled"
        player1_name.place(x=120,y=30, width=200)
        player2_label.place(x=20, y=90)
        player2_name.insert(1.0, "Bot 2")
        player2_name['state'] = "disabled"
        player2_name.place(x=120,y=90, width=200)
        # add bot 1 level
        bot1level_label.place(x=20, y=140)
        bot1_combobox.place(x=120, y=140)   
        # add bot 2 level
        bot2level_label.place(x=20, y=180)
        bot2_combobox.place(x=120, y=180)   
        start_btn['command'] = lambda: go(tk.Toplevel(root), player1_name.get(1.0, "end-1c"), player2_name.get(1.0, "end-1c"), update_bot1_level(), update_bot2_level(), 3)
        start_btn.place(x=130, y=250, width=100, height=40)

    start_window.mainloop()

def go(root, p1, p2, d1, d2, m):
    global start_window
    start_window.destroy()
    if d1 == "Easy":
        d1 = 1
        if m == 2:
            p2 += " - Easy"
        elif m == 3: 
            p1 += " - Easy"
    elif d1 == "Medium":
        d1 = 2
        if m == 2:
            p2 += " - Medium"
        elif m == 3: 
            p1 += " - Medium"
    elif d1 == "Hard":
        d1 = 3
        if m == 2:
            p2 += " - Hard"
        elif m == 3: 
            p1 += " - Hard"
    else: d1 = None
    
    if d2 == "Easy":
        d2 = 1
        p2 += " - Easy"
    elif d2 == "Medium":
        d2 = 2
        p2 += " - Medium"
    elif d2 == "Hard":
        d2 = 3
        p2 += " - Hard"
    else: d2 = None
    start(root, p1,p2,m,d1,d2)