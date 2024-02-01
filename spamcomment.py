import re

def is_spam(comment):
    # Define patterns for common spam characteristics
    patterns = [
        r"(buy|cheap|free|win|money)",
        r"\b(?:https?://)?(?:www\.)?[a-z0-9-]+(\.[a-z]{2,})+(?:[/?].*)?\b",  # Detect URLs
        r"\b\d{10,}\b"  # Detect long sequences of numbers (potential phone numbers)
    ]

    # Check if the comment matches any of the spam patterns
    for pattern in patterns:
        if re.search(pattern, comment, re.IGNORECASE):
            return True

    return False

# Example usage
comment1 = "make a lot of money"
comment2 = "Buy Now"
comment3 = "Subscribe this"
comment4 = "Buy this cheap item"

if is_spam(comment1):
    print("Comment 1 is spam.")
else:
    print("Comment 1 is not spam.")

if is_spam(comment2):
    print("Comment 2 is spam.")
else:
    print("Comment 2 is not spam.")

if is_spam(comment3):
    print("Comment 3 is spam.")
else:
    print("Comment 3 is not spam.")

if is_spam(comment4):
    print("Comment 4 is spam.")
else:
    print("Comment 4 is not spam.")