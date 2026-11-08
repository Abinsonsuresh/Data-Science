from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

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


le = LabelEncoder()

colour = le.fit_transform(colour)
car_type = le.fit_transform(car_type)
origin = le.fit_transform(origin)
stolen = le.fit_transform(stolen)

features = list(zip(colour,car_type,origin))
label = stolen

model = CategoricalNB()
model.fit(features,label)

test = [[0,0,0]]

pred = model.predict(test)
print(le.inverse_transform(pred))
print(model.score(features,label) * 100)
