import pandas as pd
import joblib
from preprocess import clean_text
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.metrics import classification_report, accuracy_score

# Load data
df = pd.read_csv("../data/tickets.csv")

# Combine text
df["text"] = df["Subject"] + " " + df["Description"]
df["text"] = df["text"].apply(clean_text)

X = df["text"]
y = df["Category"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ML Pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    ("clf", LogisticRegression(max_iter=1000))
])

# Train
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))


y_pred = pipeline.predict(X_test)

print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))


# Save model
joblib.dump(pipeline, "../model/ticket_classifier.pkl")
print("✅ Model saved successfully")
