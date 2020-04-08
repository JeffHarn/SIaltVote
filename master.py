import pandas as pd

#Getting Data
filename = input("Enter File Name: ")
fulldata = pd.ExcelFile(".\\testdata\\" + filename)
sheetname = input(r"Enter Sheet/Position Name: ")
df = fulldata.parse(sheetname)
nlist = df.values.tolist()