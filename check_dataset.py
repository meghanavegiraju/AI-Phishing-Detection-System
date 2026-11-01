
import pandas as pd

# Load dataset
data = pd.read_csv("dataset/phishing_emails.csv")

# Display first five records
print("First five emails:")
print(data.head())

# Check dataset size
print("\nDataset shape:")
print(data.shape)

# Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# Count phishing and legitimate emails
print("\nEmail distribution:")
print(data["label"].value_counts())
