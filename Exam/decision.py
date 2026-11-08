from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
x = iris.data
y = iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4,random_state=42)

model = DecisionTreeClassifier()
model.fit(x_train,y_train)
ypred = model.predict(x_test)


print("PRED:",ypred)
print("VALUES:",y_test)
print("ACCURACY:",accuracy_score(y_test,ypred) * 100,"%")
