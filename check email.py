# Simple Spam / Genuine Email Detection using Naive Bayes Concept

import re
from collections import Counter

# Function to clean and preprocess the email text
def preprocess(text):
    # Convert all text to lowercase for uniform comparison
    text = text.lower()
    # Remove special characters, numbers, and punctuation
    text = re.sub(r'[^a-z\s]', '', text)
    # Split the cleaned text into individual words
    words = text.split()
    return words

# Function to check whether the given email is spam or genuine
def check_email(email):
    # List of commonly used spam or phishing-related words
    spam_words = [
        "win", "lottery", "free", "money", "prize", "click", "urgent",
        "congratulations", "offer", "account", "suspended", "verify",
        "password", "bank", "transfer", "credit", "claim", "gift", "bonus"
    ]
    
    # List of words that are commonly seen in genuine business or normal emails
    genuine_words = [
        "meeting", "project", "schedule", "report", "information",
        "team", "discussion", "update", "plan", "work", "document",
        "details", "submission", "client", "data"
    ]

    # Preprocess the given email text
    email_words = preprocess(email)
    # Count the frequency of each word in the email
    word_count = Counter(email_words)

    spam_score = 0
    genuine_score = 0

    # Compare each word with spam and genuine lists
    for word in word_count:
        if word in spam_words:
            spam_score += word_count[word]  # Increase spam score
        elif word in genuine_words:
            genuine_score += word_count[word]  # Increase genuine score

    # Decision-making step based on the scores
    if spam_score > genuine_score:
        return " Spam or Phishing Email Detected!"
    else:
        return "Genuine Email (Safe)"

# ---- Main Program Execution ----
# Accept email text from user
email_text = input("Enter your email content: ")

# Get result by calling function
result = check_email(email_text)

# Display the final classification result
print("\nResult:", result)
