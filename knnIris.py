
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X_train, y_train)

# Predict test data
y_pred = knn.predict(X_test)

# Display results
print("Predictions:", y_pred)
print("Actual values:", y_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict a new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = knn.predict(sample)

print("Predicted class:", iris.target_names[prediction[0]])

# OUTPUT

# Predictions: [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0]
# Actual values: [1 0 2 1 1 0 1 2 1 1 2 0 0 0 0 1 2 1 1 2 0 2 0 2 2 2 2 2 0 0]
# Accuracy: 1.0
# Predicted class: setosa