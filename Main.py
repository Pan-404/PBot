import time as t
import random as r
import os
import math
import tkinter as tk
from tkinter import filedialog, Text


root = tk.Tk()


#Functions

# start function(1)
def RunBot():
    print("Starting...")
    t.sleep(1)
    print("PBot!")
    t.sleep(0.5)
    new_or_have = input("New account(new) or already have an account(login)? \n> ")
    if new_or_have == "new":
        naname = input("What is your name? \n> ")
        print("hello " + naname)
        meniu()
    elif new_or_have == "login":
        print("W.I.P")
        t.sleep(1)
        exit()

# main function(2)
def meniu():
    print("-------------------------------")
    alegere = input("1.Random. \n2. \n0.exit \n> ")
    if alegere == "1":
        randomnumber()
    elif alegere == "0":
        exit()

# function 3
def randomnumber():
    print("-------------------------------")
    randomnr = input("1.random number(0-1000) \n2.dice(1-6) \n3.coin flip(head, tails) \n0.to go back \n> ")

    if randomnr == "1":
        t.sleep(0.2)
        print(r.randrange(0,1000))
        back = input("to go back to the menu type back. \n> ")
        if back == "back":
            randomnumber()
    elif randomnr == "2":
        t.sleep(0.2)
        print(r.randrange(1,6 ))
        back = input("to go back to the menu type back \n> ")
        if back == "back":
            randomnumber()
    elif randomnr == "3":
        t.sleep(0.2)
        headortails = r.randrange(0, 1)
        if headortails == "0":
            print("head")
        else:
            print("tails")
        back = input("to go back to the menu type back \n> ")
        if back == "back":
            randomnumber()
    elif randomnr == "0":
        meniu()

#GUI

canvas = tk.Canvas(root, height=700, width=700, bg="#808080")
canvas.pack()

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

Runbot = tk.Button(root, text="Run the bot", padx=10, pady=5, fg="white", bg="green", command=RunBot)
Runbot.pack()

root.mainloop()
