import joblib
from preprocess import clean_text

model = joblib.load("../model/ticket_classifier.pkl")

def predict_ticket(subject, description):
    text = clean_text(subject + " " + description)
    return model.predict([text])[0]

if __name__ == "__main__":
    print(predict_ticket(
        "Payment failed",
        "Amount deducted but transaction not completed"
    ))
