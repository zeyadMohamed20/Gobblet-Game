import tkinter as tk
from tkinter import ttk

def contribution_screen(root):
    # Create the contribution window
    contribution_window = tk.Toplevel(root)
    contribution_window.title("Contribution")
    contribution_window.iconbitmap("./frame0/icon.ico")
    
    # Set dimensions
    width = 800
    height = 400
    contribution_window.geometry(f"{width}x{height}")
    contribution_window.configure(bg="#ECECE2")

    # Create and display the text
    text = "\nThis game is made for educational purposes under the supervision of \n\tDr. Manal Morad\n\tEng. Mahmoud Osama\nthroughout CSE472s - Artificial Intelligence Course.\n\n\nTeam Contributions:"
    text_label = tk.Label(contribution_window, text=text, wraplength=500, justify="left", font=("Helvetica", 12), bg="#ECECE2")
    text_label.pack()

    # Create and display the contributors table
    headings = ["Name", "ID", "Role"]
    contributors_data = [
        ("Mohamed Ashraf", "1901054", "Integration / Testing / Tree Expand"),
        ("Omar Osama", "2001754", "Player Vs Player Game Play / Player Vs AI Game Play"),
        ("Nervana Gamal", "1900055", "MaxMin Algorithm / Evaluation Function"),
        ("Zeyad Mohamed", "1900959", "Board Data Structure"),
        ("Malek Abdelrahman", "1901104", "Main Screen / Intermediate Screen / Documentation"),
        ("Bishoy Yousry", "1900733", "AI VS AI Game Play"),
        ("Omar Karam", "1900868", "Iterative Deepening / Tree Expand"),
        ("Yasmeen Abdelrazik", "1900434", "Cell Data structure / Alpha Beta Algorithm")
    ]

    tree = ttk.Treeview(contribution_window, columns=headings, show="headings", height=9)
    
    # Set column headings
    for heading in headings:
        tree.heading(heading, text=heading)

    # Insert data into the table
    for contributor in contributors_data:
        tree.insert("", "end", values=contributor)

    tree.pack(pady=20)
    contribution_window.resizable(False, False)    

    # Start the Tkinter event loop for the contribution window
    contribution_window.mainloop()
