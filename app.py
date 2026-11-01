
import streamlit as st
import pickle
import re
import matplotlib.pyplot as plt
from urllib.parse import urlparse

from database import (
    create_table,
    save_email,
    get_history,
    save_url,
    get_url_history
)

# Page configuration
st.set_page_config(
    page_title="Phishing Detection System",
    page_icon="🛡️",
    layout="wide"
)

# Create database
create_table()

st.title("🛡️ AI-Based Phishing Detection System")
st.write("Analyze suspicious emails and URLs.")

# Load ML model
with open("models/phishing_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/tfidf_vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# Dashboard statistics
email_records = get_history()
url_records = get_url_history()

total_emails = len(email_records)

phishing_emails = sum(
    1 for record in email_records
    if record[2] == "Phishing"
)

legitimate_emails = sum(
    1 for record in email_records
    if record[2] == "Legitimate"
)

total_urls = len(url_records)

suspicious_urls = sum(
    1 for record in url_records
    if record[3] == "Suspicious"
)

st.header("📊 Security Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Emails", total_emails)
col2.metric("Phishing Emails", phishing_emails)
col3.metric("Legitimate Emails", legitimate_emails)
col4.metric("Total URLs", total_urls)

col5, col6 = st.columns(2)

col5.metric("Suspicious URLs", suspicious_urls)
col6.metric("No Obvious URL Flags", total_urls - suspicious_urls)

st.divider()


# Email Detection
st.header("📧 Email Phishing Detection")

email = st.text_area("Enter email content:")

if st.button("Analyze Email"):
    if email.strip():
        cleaned_email = clean_text(email)
        features = vectorizer.transform([cleaned_email])
        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "Phishing"
            st.error("⚠️ This email may be PHISHING!")
        else:
            result = "Legitimate"
            st.success("This email is classified as LEGITIMATE.")

        save_email(email, result)
        st.success("Email analysis saved successfully!")

    else:
        st.warning("Please enter email content.")


st.divider()


# URL Detection
st.header("🔗 Suspicious URL Detection")

url = st.text_input("Enter URL:")

if st.button("Analyze URL"):
    if url.strip():
        parsed_url = urlparse(url)
        risk_score = 0
        reasons = []

        if parsed_url.scheme.lower() != "https":
            risk_score += 1
            reasons.append("URL does not use HTTPS")

        suspicious_words = [
            "login", "verify", "bank",
            "update", "password", "free", "claim"
        ]

        for word in suspicious_words:
            if word in url.lower():
                risk_score += 1
                reasons.append(f"Suspicious keyword: {word}")

        if risk_score >= 2:
            result = "Suspicious"
            st.error("⚠️ Suspicious URL detected!")
        else:
            result = "No obvious suspicious patterns"
            st.success(result)

        st.write("Risk Score:", risk_score)

        for reason in reasons:
            st.write("•", reason)

        save_url(url, risk_score, result)
        st.success("URL analysis saved successfully!")

    else:
        st.warning("Please enter a URL.")


# Email History
st.divider()
st.header("📧 Email Analysis History")

email_history = get_history()

if email_history:
    email_data = []

    for record in email_history:
        email_data.append({
            "ID": record[0],
            "Email": record[1],
            "Prediction": record[2],
            "Date & Time": record[3]
        })

    st.dataframe(email_data, use_container_width=True)

else:
    st.info("No email analysis history available.")


# URL History
st.divider()
st.header("🔗 URL Analysis History")

url_history = get_url_history()

if url_history:
    url_data = []

    for record in url_history:
        url_data.append({
            "ID": record[0],
            "URL": record[1],
            "Risk Score": record[2],
            "Result": record[3],
            "Date & Time": record[4]
        })

    st.dataframe(url_data, use_container_width=True)

else:
    st.info("No URL analysis history available.")


# Security Analytics
st.divider()
st.header("📊 Security Analytics")

phishing_count = sum(
    1 for record in email_history
    if record[2] == "Phishing"
)

legitimate_count = sum(
    1 for record in email_history
    if record[2] == "Legitimate"
)

suspicious_count = sum(
    1 for record in url_history
    if record[3] == "Suspicious"
)

other_url_count = len(url_history) - suspicious_count

col1, col2 = st.columns(2)


# Email Pie Chart
with col1:
    st.subheader("Email Detection Results")

    if phishing_count + legitimate_count > 0:

        fig, ax = plt.subplots()

        ax.pie(
            [phishing_count, legitimate_count],
            labels=["Phishing", "Legitimate"],
            autopct="%1.1f%%",
            startangle=90
        )

        ax.set_title("Email Classification")

        st.pyplot(fig)
        plt.close(fig)

    else:
        st.info(
            "No email analysis records available yet. "
            "Analyze an email to view this chart."
        )


# URL Bar Chart
with col2:
    st.subheader("URL Analysis Results")

    if suspicious_count + other_url_count > 0:

        fig, ax = plt.subplots()

        ax.bar(
            ["Suspicious", "No obvious flags"],
            [suspicious_count, other_url_count]
        )

        ax.set_ylabel("Number of URLs")
        ax.set_title("URL Risk Analysis")

        st.pyplot(fig)
        plt.close(fig)

    else:
        st.info(
            "No URL analysis records available yet. "
            "Analyze a URL to view this chart."
        )

st.divider()

st.caption(
    "Educational cybersecurity project. "
    "Predictions are not guaranteed security verdicts."
)
