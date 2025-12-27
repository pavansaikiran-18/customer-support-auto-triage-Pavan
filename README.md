📌 Customer Support Ticket Auto-Triage System

An end-to-end Machine Learning & NLP project that automatically classifies customer support tickets into predefined categories and enables intelligent ticket routing via a REST API.

This project is designed to reduce manual effort, improve response time, and enhance customer satisfaction.

🚀 Project Overview

Customer support teams often handle a large volume of incoming tickets. Manual triaging is time-consuming and error-prone.
This system automates the initial ticket classification process using NLP and Machine Learning.

✅ Key Capabilities

Automatic ticket classification

NLP-based text preprocessing

Real-time prediction using REST API

Clean, modular, production-ready architecture

🎯 Objectives

Automate customer support ticket triage

Classify tickets into predefined categories

Reduce manual intervention

Enable real-time classification through an API

🧠 Ticket Categories

The model classifies tickets into the following categories:

Bug Report – Application defects or crashes

Feature Request – Suggestions for new features or enhancements

Technical Issue – Server, API, or performance issues

Billing Inquiry – Payments, invoices, refunds, subscriptions

Account Management – Login, profile, or account-related issues

📁 Project Structure
customer-support-auto-triage/
│
├── venv/                 # Virtual environment (ignored in Git)
├── data/
│   └── tickets.csv       # Training dataset
├── model/
│   ├── ticket_classifier.pkl
│   └── model_metrics.json
├── src/
│   ├── preprocess.py     # NLP preprocessing
│   ├── train.py          # Model training & evaluation
│   └── predict.py        # Local inference
├── app.py                # Flask REST API
├── requirements.txt
├── .gitignore
└── README.md

🛠️ Tech Stack

Language: Python 3.8+

Libraries:

pandas, numpy

scikit-learn

NLTK

Flask

joblib

ML Model: Logistic Regression

Vectorization: TF-IDF

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/pavansaikiran-18/customer-support-auto-triage-Pavan.git
cd customer-support-auto-triage

2️⃣ Create & activate virtual environment
python -m venv venv


Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

🧪 Model Training

Run the training pipeline:

cd src
python train.py
cd ..

Output:

Trained model → model/ticket_classifier.pkl

Evaluation metrics → model/model_metrics.json

📊 Model Evaluation

Metrics used:

Accuracy

Precision

Recall

F1-Score

Metrics are saved as JSON for reproducibility and reporting.

🌐 Run the REST API
python app.py


API will be available at:

http://127.0.0.1:5000

🔌 API Usage
Endpoint
POST /predict

Request Body
{
  "subject": "Payment issue",
  "description": "Charged twice for my subscription"
}

Response
{
  "predicted_category": "Billing Inquiry"
}

🧠 Architecture Overview
Client
  ↓
Flask REST API
  ↓
Text Preprocessing (NLP)
  ↓
TF-IDF Vectorizer
  ↓
ML Classifier
  ↓
Predicted Ticket Category

📌 Git & Environment Management

Virtual environment (venv/) is ignored using .gitignore

Dependencies are tracked via requirements.txt

Clean commit history following conventional commits

🧾 Resume-Ready Description

Developed an end-to-end ML-based Customer Support Ticket Auto-Triage system using NLP and Logistic Regression, enabling automated ticket classification and real-time routing via a REST API.

🔮 Future Enhancements

Priority prediction

Deep learning models (BERT / Transformers)

Dashboard for analytics

Cloud deployment (Docker, AWS/GCP)

Multilingual ticket support

👨‍💻 Author

Nerella Pavan Sai Kiran
AI / ML • Data Analytics • Software Development