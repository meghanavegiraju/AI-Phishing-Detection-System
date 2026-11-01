# 🛡️ AI-Based Phishing Email & Malicious URL Detection System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-phishing-detection-system-f4jzjuqmbx3kukf8cg2j43.streamlit.app/)

## 🌐 Live Application

**Try the project here:**  
https://ai-phishing-detection-system-f4jzjuqmbx3kukf8cg2j43.streamlit.app/

## 📌 Project Overview

The AI-Based Phishing Email & Malicious URL Detection System is a Python-based cybersecurity application designed to identify potentially phishing emails and suspicious URLs.

It uses Machine Learning techniques to classify email messages and rule-based analysis to identify suspicious URL patterns. The application provides an interactive Streamlit dashboard for analyzing results and viewing security statistics.

## ✨ Features

- **Email Phishing Detection:** Classifies emails as phishing or legitimate using Machine Learning.
- **Text Preprocessing:** Cleans email text before analysis.
- **TF-IDF Vectorization:** Converts email text into numerical features.
- **Logistic Regression:** Machine Learning algorithm for email classification.
- **Suspicious URL Detection:** Identifies suspicious URL patterns using security rules.
- **Analysis History:** Stores email and URL analysis results using SQLite.
- **Security Dashboard:** Displays email and URL analysis statistics.
- **Data Visualization:** Presents analysis results through charts using Matplotlib.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | Web application |
| Pandas | Dataset processing |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Logistic Regression | Email classification |
| SQLite | Database |
| Matplotlib | Data visualization |

## 📂 Project Structure

```text
AI-Phishing-Detection-System/
│
├── dataset/
│   └── phishing_emails.csv
│
├── models/
│   ├── phishing_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── app.py
├── train_model.py
├── email_analyzer.py
├── url_analyzer.py
├── preprocessing.py
├── database.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd AI-Phishing-Detection-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```powershell
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Train the Machine Learning model

```bash
python train_model.py
```

### 7. Run the application

```bash
streamlit run app.py
```

## 🔍 How It Works

1. User enters email content or a URL.
2. Email text is cleaned and preprocessed.
3. TF-IDF converts email text into numerical features.
4. Logistic Regression predicts whether the email may be phishing or legitimate.
5. URL analysis checks for suspicious patterns.
6. Results are stored in the SQLite database.
7. The Streamlit dashboard displays analysis history and statistics.

## 📊 Application Modules

- Email Phishing Detection
- Suspicious URL Detection
- Email Analysis History
- URL Analysis History
- Security Overview Dashboard
- Security Analytics and Charts

## 🎯 Project Objective

The objective of this project is to demonstrate how Machine Learning and basic cybersecurity techniques can be combined to identify potentially phishing emails and suspicious URLs through an interactive web application.

## ⚠️ Disclaimer

This is an educational cybersecurity project. The email model was trained using a small sample dataset, and URL analysis uses basic rule-based checks. Predictions are not guaranteed to identify malicious content and should not be used as the sole basis for real-world security decisions.

## 👩‍💻 Author

**Meghana Vegiraju**  
B.Tech – Artificial Intelligence and Data Science  
2026 Graduate

**Project:** AI-Based Phishing Email & Malicious URL Detection System
