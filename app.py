from flask import Flask, request, jsonify
import joblib
from src.preprocess import clean_text

app = Flask(__name__)
model = joblib.load("model/ticket_classifier.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    subject = data.get("subject", "")
    description = data.get("description", "")
    
    text = clean_text(subject + " " + description)
    prediction = model.predict([text])[0]
    
    return jsonify({
        "predicted_category": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)
