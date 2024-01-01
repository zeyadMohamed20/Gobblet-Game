import tkinter as tk
from optionScreen import options_screen
from contributionScreen import contribution_screen
from controlFunctions import play_click_sound
from startScreen import showStart

def main_screen():
    # Create the main window
    main_window = tk.Tk()
    main_window.title("Goblet Game")
    
    # Set dimensions
    width = 450
    height = 650
    main_window.geometry(f"{width}x{height}")
    main_window.resizable(False, False)   
    main_window.iconbitmap("./frame0/icon.ico")
    main_window.configure(bg="#B9A180")
 

    # Create and center the title label
    title_label = tk.Label(main_window, text="Time to Gobble!", font=("Georgia", 30), bg="#B9A180")
    title_label.pack(pady=60)

    # Create and center the buttons with constant spacing
    button_width = 25
    button_height = 2
    button_spacing = 5

    button1 = tk.Button(main_window, text="Player Vs Player", font=("Supply Center", 14), cursor="hand2", width=button_width,bg="#997950",activebackground="#4B382A", borderwidth=5, height=button_height, command=lambda: showStart(main_window, 1))
    button1.pack(side="top", pady=button_spacing)
    
    button2 = tk.Button(main_window, text="Player Vs AI", font=("Supply Center", 14), cursor="hand2", width=button_width,bg="#997950",activebackground="#4B382A", borderwidth=5, height=button_height, command=lambda: showStart(main_window, 2))
    button2.pack(side="top", pady=button_spacing)

    button3 = tk.Button(main_window, text="AI Vs AI", font=("Supply Center", 14), cursor="hand2", width=button_width,bg="#997950",activebackground="#4B382A", borderwidth=5, height=button_height, command=lambda: showStart(main_window, 3))
    button3.pack(side="top", pady=button_spacing)

    button4 = tk.Button(main_window, text="Options", font=("Supply Center", 14), cursor="hand2", width=button_width,bg="#997950",activebackground="#4B382A", height=button_height, borderwidth=5, command=lambda: options_screen(main_window))
    button4.pack(side="top", pady=button_spacing)

    button5 = tk.Button(main_window, text="Contribution", font=("Supply Center", 14), cursor="hand2", width=button_width,bg="#997950",activebackground="#4B382A", height=button_height, borderwidth=5, command=lambda: contribution_screen(main_window))
    button5.pack(side="top", pady=button_spacing)


    # Bind the play_click_sound function to the mouse click event for the main window
    main_window.bind("<Button-1>", lambda event: play_click_sound())

    # Start the Tkinter event loop
    main_window.mainloop()
