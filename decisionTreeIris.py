from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y= iris.target
# print(iris)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(x_train,y_train)

plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True
)

plt.title("Decision Tree using Iris Dataset")
plt.show()
