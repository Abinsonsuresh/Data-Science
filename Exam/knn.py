from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
x = iris.data
y = iris.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(x_train,y_train)
ypred = model.predict(x_test)

print("PRED:",ypred)
print("VALUES:",y_test)
print("ACCURACY:",accuracy_score(y_test,ypred))


sample = [[5,3,2,4]]
p = model.predict(sample)
print(iris.target_names[p])