import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

energy = pd.read_csv("energy_data.csv",sep="\t")

X = energy['Year'].to_numpy()
y = energy['Non-domestic consumption (kWh)'].to_numpy()

model = LinearRegression()
model = model.fit(X.reshape(-1, 1), y.reshape(-1, 1))

future_X = np.arange(2022, 2042, 1)

plt.scatter(X, y)
print(model.coef_, " ", model.intercept_)
y_predicted = X * model.coef_ + model.intercept_[0]
print(y_predicted, " ", X)
plt.plot(X, y_predicted.ravel())
plt.show()

print(model.coef_ * 2050 + model.intercept_)