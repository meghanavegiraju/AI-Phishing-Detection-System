
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer

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

print("Original email:")
print(data["email_text"][0])

print("\nCleaned email:")
print(data["cleaned_email"][0])

print("\nTF-IDF matrix shape:")
print(X.shape)

print("\nTarget labels:")
print(y.values)
