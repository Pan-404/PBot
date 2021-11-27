import time as t
import random as r
import os
import math
import tkinter as tk
from tkinter import filedialog, Text

root = tk.Tk()

#Functii

def RunBot():
    print("Starting...")
    t.sleep(1)
    print("Welcome! To the Alexander-Bot")
    t.sleep(0.5)
    new_or_have = input("New account(new) or already have an account(skip)?: ")
    if new_or_have == "new":
        name = input("What is your name?: ")
        print("Hello " + name)
    elif new_or_have == "skip":
        print("sa ma sugi de poponet XD L")
        
#GUI

canvas = tk.Canvas(root, height=700, width=700, bg="#808080")
canvas.pack()

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

Runbot = tk.Button(root, text="Run the bot", padx=10, pady=5, fg="white", bg="green", command=RunBot)
Runbot.pack()

root.mainloop()
