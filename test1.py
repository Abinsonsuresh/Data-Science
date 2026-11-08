import numpy as np
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

# Dataset
colour = [
    'Red', 'Red', 'Red', 'Yellow', 'Yellow',
    'Yellow', 'Yellow', 'Yellow', 'Red', 'Red'
]

car_type = [
    'sports', 'sports', 'sports', 'sports', 'sports',
    'SUV', 'SUV', 'SUV', 'SUV', 'sports'
]

origin = [
    'domestic', 'domestic', 'domestic', 'domestic',
    'imported', 'imported', 'imported', 'domestic',
    'imported', 'imported'
]

stolen = [
    'yes', 'no', 'yes', 'no', 'yes',
    'no', 'yes', 'no', 'no', 'yes'
]

# Encode categorical data
le1 = LabelEncoder()
le2 = LabelEncoder()
le3 = LabelEncoder()
le4 = LabelEncoder()

colour = le1.fit_transform(colour)
car_type = le2.fit_transform(car_type)
origin = le3.fit_transform(origin)
stolen = le4.fit_transform(stolen)

# Combine features
features = list(zip(colour, car_type, origin))

label = stolen

# Create and train model
model = CategoricalNB()
model.fit(features, label)

# Predict for new car
# Colour=Red, Type=SUV, Origin=domestic

test = [[
    le1.transform(['Red'])[0],
    le2.transform(['SUV'])[0],
    le3.transform(['domestic'])[0]
]]

predicted = model.predict(test)

print("Prediction:", le4.inverse_transform(predicted)[0])

# Calculate accuracy
print("Accuracy:", model.score(features, label) * 100, "%")




import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Input data
X = np.array([95, 85, 80, 70, 60]).reshape(-1, 1)

y = np.array([85, 95, 70, 65, 70])

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict statistics grade for aptitude score 80
prediction = model.predict([[80]])

print("Slope:", model.coef_[0])

print("Intercept:", model.intercept_)

print("Predicted Statistics Grade:")
print(round(prediction[0], 2))

# Plot graph
plt.scatter(X, y, label="Actual Data")

plt.plot(
    X,
    model.predict(X),
    label="Regression Line"
)

plt.title("Simple Linear Regression")
plt.xlabel("Aptitude Score")
plt.ylabel("Statistics Grade")

plt.legend()
plt.grid()

plt.show()


import pandas as pd

# Create student data
data = {
    "Roll.no": [1, 2, 3, 4, 5],
    "Name": ["Anu", "Nikhil", "Neha", "Rahul", "Naveen"],
    "Age": [18, 19, 18, 20, 19],
    "Marks": [85, 75, 92, 68, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)

# a. Select top 2 rows
print("\nTop 2 Rows:")
print(df.head(2))

# b. Filter marks greater than 80
print("\nStudents with Marks Greater than 80:")
print(df[df["Marks"] > 80])

# c. Names starting with N
print("\nNames Starting with N:")
print(df[df["Name"].str.startswith("N")])