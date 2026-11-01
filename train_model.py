import pandas as pd
import re
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("dataset/phishing_emails.csv")

# Clean email text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

data["cleaned_email"] = data["email_text"].apply(clean_text)

# Convert text into numerical features
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(data["cleaned_email"])
y = data["label"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer
with open("models/phishing_model.pkl", "wb") as file:
    pickle.dump(model, file)

with open("models/tfidf_vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

print("Model trained successfully!")
print("Model and vectorizer saved in models folder.")