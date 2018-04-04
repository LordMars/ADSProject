import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats, integrate
import statsmodels.api as sm


def VisualizeCount(data):
  print("Count: " + str(data.count()))

def VisualizeMean(data):
  print("Mean: " + str(data.mean()))

def VisualizeMaxMinMeanMedianQuantileRange(data):
  print("Minimum: " + str(data.min()))
  print("Maximum: " + str(data.max()))
  print("Median: " + str(data.median()))
  print("Quartile: " + str(data.quantile(0.25)))
  print("Range: " + str(data.max() - data.min()))

  # Whisker/BoxPlot for Minimum, Max, etc.
  plt.figure()
  plt.boxplot(data)
  plt.show()


def VisualizeMode(data):
  print("Mode: " + str(data.mode()[0]))

  # Frequency Diagram
  plt.hist(data)
  plt.title("Frequency diagram")
  plt.xlabel("Value")
  plt.ylabel("Frequency")
  plt.show()

def VisualizeVarAndStd(data):
  print("Variance: " + str(data.var()))
  print("Standard Deviation: " + str(data.std()))

def VisualizeCodAndSkew(data):
  print("COV: ")
  print("Skewness:  " + str(data.skew()))
  print("Kurtosis: " + str(data.kurtosis()))

  x = range(1,151)
  y = data


  plt.scatter(x, y, 3, 'red', alpha=0.5)
  plt.grid(True)
  plt.show()


def AnalyzeColumn(data):
  VisualizeCount(data)
  VisualizeMean(data)
  VisualizeMaxMinMeanMedianQuantileRange(data)
  VisualizeMode(data)
  VisualizeVarAndStd(data)
  VisualizeCodAndSkew(data)

def AnalyzeSingleRegression(data):
  x = data.copy()

  # Tryna to generate a column with 1-50 cause
  # I couldnt get range(1,51) or anything else to
  # work cause I'm trash at python. - Delaney
 
  count = 0
  for i in x:
    x[count] = count + 1
    count += 1 

  y = data

  fig, ax = plt.subplots()
  fit = np.polyfit(x, y, deg=1)
  ax.plot(x, fit[0]*x+fit[1], color='red')
  ax.scatter(x, y)

  plt.show()

def AnalyzeMultipleRegression():
  xlpath = "crime.xls"

  data = pd.read_excel(xlpath, header=0, error_bad_lines=False)
  #print("\n{}\n".format(data))

  targets = pd.DataFrame(data, columns=["X1"])

  X = data[["X2","X3","X4","X5","X6","X7"]]
  y = targets["X1"]
  X = sm.add_constant(X)

  model = sm.OLS(y, X).fit()
  predictions = model.predict(X)

  plt.scatter(predictions, y, s=30, c='r', marker='+', zorder=10)
  fit = np.polyfit(predictions, y, deg=1)
  plt.plot(predictions, fit[0] * predictions + fit[1], color='orange')
  plt.xlabel("Predicted Values from model")
  plt.ylabel("Actual Values Prices")
  plt.show()

  
def main():

  choice = raw_input("Do you want to analyze Iris or Crime Data?(I/C):")

  if(choice == 'I'):
    print("Analyzing Iris...")
    xls = pd.ExcelFile("Iris.xls")

    # Parse sheet 1
    Sheet = xls.parse(0)

    column1 = Sheet['sepal length']
    column2 = Sheet['sepal width']
    column3 = Sheet['petal length']
    column4 = Sheet['petal width']


    print("\n\n_________________________________\nANALYZING SEPAL LENGTH\n_________________________________\n\n")
    AnalyzeColumn(column1)
    print("\n\n_________________________________\nANALYZING SEPAL WIDTH\n_________________________________\n\n")
    AnalyzeColumn(column2)
    print("\n\n_________________________________\nANALYZING PETAL LENGTH\n_________________________________\n\n")
    AnalyzeColumn(column3)
    print("\n\n_________________________________\nANALYZING PETAL LENGTH\n_________________________________\n\n")
    AnalyzeColumn(column4)

  elif(choice == 'C'):
    print("Analyzing Crime...")
    xls = pd.ExcelFile("crime.xls")

    # Parse sheet 1
    Sheet = xls.parse(0)

    X1 = Sheet['X1']
    X2 = Sheet['X2']
    X3 = Sheet['X3']
    X4 = Sheet['X4']
    X5 = Sheet['X5']
    X6 = Sheet['X6']
    X7 = Sheet['X7']

    AnalyzeSingleRegression(X1)
    AnalyzeSingleRegression(X2)
    AnalyzeSingleRegression(X3)
    AnalyzeSingleRegression(X4)
    AnalyzeSingleRegression(X5)
    AnalyzeSingleRegression(X6)
    AnalyzeSingleRegression(X7)

    AnalyzeMultipleRegression()
  
if __name__ == "__main__":
  main()
