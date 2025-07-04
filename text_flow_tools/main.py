import re
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter

class TextProcessor:
    def __init__(self):
        self.stemmer = PorterStemmer()

    def clean_text(self, text):
        # Remove special characters and numbers, convert to lowercase
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text.lower()

    def tokenize_text(self, text):
        # Tokenize text into words
        return word_tokenize(text)

    def stem_word(self, word):
        # Stem a single word
        return self.stemmer.stem(word)

    def analyze_frequency(self, tokens):
        # Analyze word frequency
        return Counter(tokens)

    def basic_sentiment_analysis(self, text):
        # Very basic sentiment analysis based on keywords
        positive_words = ["good", "great", "excellent", "positive", "happy", "love"]
        negative_words = ["bad", "poor", "terrible", "negative", "sad", "hate"]

        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)

        if positive_count > negative_count:
            return "Positive"
        elif negative_count > positive_count:
            return "Negative"
        else:
            return "Neutral"




    def count_words(self, text):
        # Count the number of words in a text
        words = word_tokenize(text)
        return len(words)


