from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder


chills = ['Y', 'Y', 'Y', 'N', 'N', 'N', 'N', 'Y']

running_nose = ['N', 'Y', 'N', 'Y', 'N', 'Y', 'Y', 'Y']

headache = ['mild', 'no', 'strong', 'mild',
            'no', 'strong', 'strong', 'mild']

fever = ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'Y']

has_flu = ['N', 'Y', 'Y', 'Y', 'N', 'Y', 'N', 'Y']

le1 = LabelEncoder()

chills = le1.fit_transform(chills)
running_nose = le1.fit_transform(running_nose)
headache = le1.fit_transform(headache)
fever = le1.fit_transform(fever)
has_flu = le1.fit_transform(has_flu)

features = list(zip(chills,running_nose,headache,fever))
label = has_flu

model = CategoricalNB()
model.fit(features,label)

test = [[1,0,0,1]]

pred = model.predict(test)
print("PRED",le1.inverse_transform(pred))
print("ACCU",model.score(features,label))