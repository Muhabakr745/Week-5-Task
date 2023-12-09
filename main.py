from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

# Load the Iris dataset
iris = load_iris()
x, y = iris.data, iris.target

# Create and train the model
model = LogisticRegression(max_iter=1000)
model.fit(x, y)

# Save the model
joblib.dump(model, 'iris_model.pkl')
