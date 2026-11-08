from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


x = np.array([95,85,80,70,60]).reshape(-1,1)
y= np.array([85,95,70,65,70])

model = LinearRegression()
model.fit(x,y)

pred = model.predict([[80]])
print(pred[0])
print(model.intercept_)
print(model.coef_)

# plt.scatter(x, y, label="Actual Data")

# plt.plot(
#     x,
#     model.predict(x),
#     label="Regression Line"
# )

# plt.title("Simple Linear Regression")
# plt.xlabel("Aptitude Score")
# plt.ylabel("Statistics Grade")


# plt.show()