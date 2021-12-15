from flask import Flask, request
from joblib import load

decision_tree = load("iris_classifier.joblib")

IRIS_CLASS_NAMES = {0: "Iris-Setosa", 1: "Iris-Versicolour", 2: "Iris-Virginica"}

app = Flask(__name__)

PORT = 4100


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/score", methods=["POST"])
def score_inputs():
    content = request.json
    val_to_score = content["values"]

    result = decision_tree.predict([val_to_score])

    iris_name_result = IRIS_CLASS_NAMES[result[0]]

    return {"result": iris_name_result}


if __name__ == "__main__":
    app.run(threaded=True, port=PORT)
