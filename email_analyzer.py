import pickle
import re

# Load trained model
with open("models/phishing_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load TF-IDF vectorizer
with open("models/tfidf_vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# Clean email
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# Predict email
def analyze_email(email):
    cleaned_email = clean_text(email)

    features = vectorizer.transform([cleaned_email])
    prediction = model.predict(features)[0]

    if prediction == 1:
        print("WARNING: This email may be PHISHING!")
    else:
        print("This email is classified as LEGITIMATE.")

# Get email from user
email = input("Enter email text: ")

analyze_email(email)