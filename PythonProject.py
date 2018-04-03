import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xls = pd.ExcelFile("../csvs/Iris.xls.xlsx")


# Parse sheet 1
Sheet = xls.parse(0) 

column1 = Sheet['sepal length']
column2 = Sheet['sepal width']
column3 = Sheet['petal length']
column4 = Sheet['petal width']

#The 'column1' below show be replaced with a variable
#in a function to make it abitrary and applicable to 
# any column. its just i dont know functions in py - d.ramalho

print("Count: " + str(column1.count()))
print("Mean: " + str(column1.mean()))
print("Minimum: " + str(column1.min()))
print("Maximum: " + str(column1.max()))
print("Median: " + str(column1.median()))
print("Mode: " + str(column1.mode()[0]))
print("Quartile: " + str(column1.quantile(0.25)))
print("Range: " + str(column1.max() - column1.min()))
print("Variance: " + str(column1.var()))
print("Standard Deviation: " + str(column1.std()))
print("COV: ")
print("Skewness:  " + str(column1.skew()))
print("Kurtosis: " + str(column1.kurtosis()))

 
fig, sct = plt.subplots()
ind = [x+2 for x,y in enumerate(column1)]

for c, col in zip(('red', 'blue', 'green', 'yellow'), (column1, column2, column3, column4)):
    plt.scatter(ind, col,
    color=c,
    s= 40,
    alpha=0.5)


sct.set_xlabel("Index")
sct.set_ylabel("Value")
sct.legend(loc="upper right")
sct.grid(True)
plt.show()
