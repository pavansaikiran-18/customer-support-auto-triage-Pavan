Customer Support Ticket Auto-Triage System

An end-to-end Machine Learning and NLP-based system that automatically classifies customer support tickets and enables intelligent routing through a RESTful API.

This project demonstrates professional ML engineering practices, including clean architecture, reproducible environments, model evaluation, and API deployment.

📌 Overview

Customer support teams handle a high volume of tickets daily.
Manual triaging is time-consuming, inconsistent, and does not scale.

This project automates the initial ticket classification process, helping organizations:

Reduce manual effort

Improve response time

Enhance customer satisfaction

❓ Problem Statement

Manual categorization of support tickets:

Is inefficient at scale

Introduces human error

Slows down issue resolution

✅ Solution

The system uses Natural Language Processing (NLP) and Machine Learning to automatically classify tickets into predefined categories and expose predictions via a REST API.

🧠 Ticket Categories

The model classifies tickets into the following categories:

Bug Report

Feature Request

Technical Issue

Billing Inquiry

Account Management

🏗️ System Architecture
Client / User
      ↓
Flask REST API
      ↓
Text Preprocessing (NLP)
      ↓
TF-IDF Vectorization
      ↓
ML Classification Model
      ↓
Predicted Ticket Category

📁 Project Structure
customer-support-auto-triage/
│
├── data/
│   └── tickets.csv
│
├── model/
│   ├── ticket_classifier.pkl
│   └── model_metrics.json
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

🛠️ Tech Stack

Language: Python 3.8+

Libraries:

pandas

numpy

scikit-learn

NLTK

Flask

joblib

Model: Logistic Regression

Vectorization: TF-IDF

Version Control: Git

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/pavansaikiran-18/customer-support-auto-triage-Pavan.git
cd customer-support-auto-triage

2️⃣ Create and Activate Virtual Environment
python -m venv venv


Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🧪 Model Training
cd src
python train.py
cd ..

Outputs

Trained model: model/ticket_classifier.pkl

Evaluation metrics: model/model_metrics.json

📊 Model Evaluation

The model is evaluated using:

Accuracy

Precision

Recall

F1-Score

Evaluation metrics are stored for reproducibility and reporting.

🌐 Running the API
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

🧩 Best Practices Followed

Modular and scalable project structure

Reproducible environments using requirements.txt

Clean Git history with conventional commits

.gitignore for virtual environment and artifacts

Separation of training and inference logic

📝 Resume-Ready Summary

Built a production-ready NLP-based Machine Learning system to automatically classify customer support tickets. Implemented end-to-end ML pipeline with evaluation and deployed predictions via a Flask REST API.

🔮 Future Enhancements

Priority prediction

Transformer-based models (BERT)

Analytics dashboard

Docker and cloud deployment

Multilingual ticket support

👨‍💻 Author

Nerella Pavan Sai Kiran
Machine Learning • Data Analytics • Software Development
