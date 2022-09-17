import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook


# # var = pd.read_excel('C:\\Users\\AKASH\\OneDrive\\Desktop\\SG\\test.xlsx')
# xl = pd.ExcelFile("C:\\Users\\AKASH\\OneDrive\\Desktop\\SG\\test.xlsx")
# df = xl.parse('Sheet1')


# # print(var)


# # x = list(var['X'])
# # y = list(var['Y'])
# # z = list(var['Z'])

# print(df['y'][2])


# # ax = plt.axes(projection='3d')

# # # ax.scatter3D(x,y,z)

# # plt.show()


import xlwings as xw

ws = xw.Book("test.xlsx").sheets['Sheet1']


x1 = ws.range("A2:A10").value
y1 = ws.range("B2:B10").value
z1 = ws.range("C2:C10").value

# v2 = ws.range("F5").value

print("Result: ",x1,y1,z1)



ax = plt.axes(projection='3d')

ax.scatter3D(x1,y1,z1)

plt.show()


