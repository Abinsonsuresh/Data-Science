from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

iris = load_iris()
x = iris.data
y= iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = svm.SVC(kernel='linear')
model.fit(x_train,y_train)

pred = model.predict(x_test)
print("Actual values:", y_test)
print("Predicted values:", pred)
print("ACCU:", accuracy_score(y_test,pred))
