import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats, integrate
import statsmodels.api as sm

xlpath = "mlr06.xls"

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