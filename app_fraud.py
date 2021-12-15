from flask import Flask, request
from joblib import load

decision_tree = load("model.joblib")

DECISION = {0: "Not Fraud", 1: "Fraud"}

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

    fraud_result = DECISION[result[0]]

    return {"result": fraud_result}


if __name__ == "__main__":
    app.run(threaded=True, port=PORT)
