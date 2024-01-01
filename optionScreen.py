import tkinter as tk
from tkinter import ttk
from controlFunctions import update_music_volume, update_game_sound_volume, play_click_sound

def options_screen(root):
    # Create the options window
    options_window = tk.Toplevel(root)
    options_window.title("Options")
    
    # Set dimensions
    width = 300
    height = 200
    options_window.geometry(f"{width}x{height}")
    options_window.iconbitmap("./frame0/icon.ico")
    options_window.configure(bg="#B9A180")

    # Create and center the sound volume adjustment
    sound_label = tk.Label(options_window, text="Game Sound Volume:", bg="#B9A180")
    sound_label.place(x=10, y=20)

    sound_scale = tk.Scale(options_window, from_=0, to=100, orient=tk.HORIZONTAL, command=update_game_sound_volume, bg="#B9A180", bd=0, border=0, highlightthickness=0, troughcolor="#997950", activebackground="#4B382A")
    sound_scale.set(update_game_sound_volume())  # Set initial value
    sound_scale.place(x=150, y=20)

    # Create and center the music volume adjustment
    music_label = tk.Label(options_window, text="Game Music Volume:", bg="#B9A180")
    music_label.place(x=10, y=100)

    music_scale = tk.Scale(options_window, from_=0, to=100, orient=tk.HORIZONTAL, command=update_music_volume, bg="#B9A180", bd=0, border=0, highlightthickness=0, troughcolor="#997950", activebackground="#4B382A")
    music_scale.set(update_music_volume())  # Set initial value
    music_scale.place(x=150, y=100)

    # Bind the play_click_sound function to the mouse click event for the option window
    options_window.bind("<Button-1>", lambda event: play_click_sound())

    # Start the Tkinter event loop for the options window
    options_window.mainloop()
