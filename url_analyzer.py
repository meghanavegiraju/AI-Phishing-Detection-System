from urllib.parse import urlparse

def analyze_url(url):

    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()

    risk_score = 0
    reasons = []

    # Check HTTPS
    if parsed_url.scheme != "https":
        risk_score += 1
        reasons.append("URL does not use HTTPS")

    # Check suspicious words
    suspicious_words = [
        "login", "verify", "bank", "update",
        "password", "free", "claim"
    ]

    for word in suspicious_words:
        if word in url.lower():
            risk_score += 1
            reasons.append(f"Suspicious keyword: {word}")

    # Check IP address usage
    if any(char.isdigit() for char in domain) and "." in domain:
        risk_score += 1
        reasons.append("Domain may contain an IP address")

    print("\nURL Analysis Result")

    if risk_score >= 2:
        print("WARNING: Suspicious URL detected!")
    else:
        print("No obvious suspicious patterns detected.")

    print("Risk Score:", risk_score)

    for reason in reasons:
        print("-", reason)


url = input("Enter URL: ")
analyze_url(url)