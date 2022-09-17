import pandas as pd
import matplotlib.pyplot as plt
from numpy import random
import numpy as np


np.random.seed(31)

m = 3
n=100



x = np.random.normal(m,1,size=n)
y = np.random.normal(m,1,size=n)
z = np.random.normal(m,1,size=n)



ax = plt.axes(projection='3d')

ax.scatter3D(x,y,z)

plt.show()
