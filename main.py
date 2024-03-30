from tkinter import *
from tkinter.ttk import Combobox
import random
root = Tk()
root.geometry("400x300")
root.title("Генератор паролей")
root.configure(background ="bisque")
def gen():
    global sc1
    sc1.set("")
    passw=("")
    length=int(sc1.get())