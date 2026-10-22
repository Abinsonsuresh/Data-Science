
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data[:, 0:1]
y = iris.data[:, 1]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Display results
print("Coefficients:")
print(model.coef_)

print("Mean squared error:")
print(mean_squared_error(y, y_pred))

print("Coefficient of determination:", model.score(X, y))

plt.scatter(X, y, color='black')
plt.plot(X, y_pred, color='blue', linewidth=3)

plt.xticks()
plt.yticks()
plt.show()

# OUTPUT

# Coefficients:
# [-0.0618848]
# Mean squared error:
# 0.18610437589381357
# Coefficient of determination: 0.013822654141080748