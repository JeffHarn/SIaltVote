import pandas as pd
import functions as fu
import copy
import time

#Getting Data
'''
Log 1
Somehow the list.remove() managed to modify a global variable
even though we use it on a dummy variable created within the function. (very weird, I might do something wrong though.)
I blame it on memory manipulation and such of the interpreter.
So we need to get the raw data multiple times, thus we define a new function.

Log 2
After some consideration and google searches, it appears that
lists are mutable objects.
Today I Learned.
'''
filename = input("Enter File Name: ")
fulldata = pd.ExcelFile(".\\testdata\\" + filename)
sheetname = input(r"Enter Sheet/Position Name: ")
df = fulldata.parse(sheetname)
available = int(input("Enter the number of slots available for this position: "))

start_time = time.time()

nlist = df.values.tolist()

#Interpreting Nested List Data

won = []

j=0
while j < available:
    itera = copy.deepcopy(nlist)
    print("Finding slot", j+1)
    print(itera)
    staticloopnum = len(itera[0])
    i=0
    #Today I learned that functions in conditional statement of loops are dynamic.
    while i < staticloopnum-1:
        print(fu.getfirstmin(itera)[0][0],"has only",fu.getfirstmin(itera)[0][1],"votes.")
        print(fu.getfirstmin(itera)[0][0],"is eliminated.")
        itera = fu.remfromnlist(itera, fu.getfirstmin(itera)[0][0])
        print("After elimination",i+1,":")
        print(itera)
        i += 1
    won.append(itera[0][0])
    print(won, "won.")
    nlist = fu.remfromnlist(nlist,won[j])
    j += 1
print(won)
print("Execution time:",time.time()-start_time,"seconds")
