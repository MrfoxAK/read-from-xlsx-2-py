from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import xlwings as xw

root = Tk()
root.geometry("444x444")


def hello():
    print("Hello Guys!")


f = Frame(root, borderwidth=7, bg="grey", relief=SUNKEN)


def name():
    print("Name is AKash")


f.pack()


def show():
    ws = xw.Book("./res/test.xlsx").sheets['Sheet1']

    x1 = ws.range("A2:A10").value
    y1 = ws.range("B2:B10").value
    z1 = ws.range("C2:C10").value

    # v2 = ws.range("F5").value

    print("Result: ", x1, y1, z1)

    ax = plt.axes(projection='3d')

    ax.scatter3D(x1, y1, z1)

    plt.show()

# from excel_2_py import show


b1 = Button(f, fg="blue", text="Click", command=show)
b1.pack(padx=25)


root.mainloop()
