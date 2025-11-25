import re 

POSITVE_WORDS = {
    "good", "great", "excellent", "amazing", "fantastic", "love", "like", "happy", "joy", "wonderful"
}

NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "hate", "dislike", "sad", "angry", "horrible", "worst", "pain"
}

def _normalize_text(text):
    """Normalize text by converting to lowercase and removing non-alphanumeric characters."""
    text = text.lower()
    words = re.findall(r'\w+', text, flags=re.UNICODE)
    return words


def analyze_sentiment(text):
    """Analyze the sentiment of the given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary with counts of positive and negative words.
    """
    words = _normalize_text(text)
    has_positive = any(word in POSITVE_WORDS for word in words)
    has_negative = any(word in NEGATIVE_WORDS for word in words)

    if has_positive and not has_negative:
        label = "positive"
    elif has_negative and not has_positive:
        label = "negative"
    else:
        label = "neutral"

    
    return {
        "label": label,
        "detail": {
            "positive_word_found": [word for word in words if word in POSITVE_WORDS],
            "negative_word_found": [word for word in words if word in NEGATIVE_WORDS]
        }
    }