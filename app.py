from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('iris_model.pkl')


@app.route('/')
def home():
    return 'Flask App is running!'


@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.get_json(force=True)
    features = [float(data['feature1']), float(data['feature2']), float(data['feature3']), float(data['feature4'])]

    # Make a prediction using the loaded model
    prediction = model.predict([features])

    # Return the prediction in JSON format
    return jsonify(prediction.tolist())


if __name__ == '__main__':
    app.run(debug=True)
