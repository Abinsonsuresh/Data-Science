
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB


X = [
    ['Y', 'N', 'mild', 'Y'],
    ['Y', 'Y', 'no', 'N'],
    ['Y', 'N', 'strong', 'Y'],
    ['N', 'Y', 'mild', 'Y'],
    ['N', 'N', 'no', 'N'],
    ['N', 'Y', 'strong', 'N'],
    ['N', 'Y', 'strong', 'N'],
    ['Y', 'Y', 'mild', 'Y']
]

y = ['N', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y']

# Encode categorical data
encoders = [LabelEncoder() for i in range(4)]
X = list(zip(*X))

X = [encoders[i].fit_transform(X[i]) for i in range(4)]
X = list(zip(*X))

le = LabelEncoder()
y = le.fit_transform(y)

# Train model
model = CategoricalNB()
model.fit(X, y)

# Test patient: chills=Y, running nose=N,
# headache=mild, fever=Y
test = [[
    encoders[0].transform(['Y'])[0],
    encoders[1].transform(['N'])[0],
    encoders[2].transform(['mild'])[0],
    encoders[3].transform(['Y'])[0]
]]

# Prediction
result = model.predict(test)
print("Has flu:", le.inverse_transform(result)[0])

# OUTPUT
# Has flu: Y