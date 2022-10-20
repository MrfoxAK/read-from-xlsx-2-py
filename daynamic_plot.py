import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import time
import pandas as pd
from matplotlib import animation

data = pd.read_csv("C:\\Users\\AKASH\\OneDrive\\Desktop\\SG\\sample.csv")

# y = data["a"]

# x = data["d"]


def plot_data(i):
    y = data["a"]
    x = data["d"]
    plt.scatter(x,y)

anime = animation.FuncAnimation(plt.gcf(),plot_data,interval=1500)

# plt.plot(x,y)
# plt.scatter(x,y)

plt.show()


















