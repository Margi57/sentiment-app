import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import re
# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# Initialize NLTK tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
sia = SentimentIntensityAnalyzer()


def preprocess_text(text):
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Tokenize words
    words = word_tokenize(text)
    
    # Remove stopwords and lemmatize words
    filtered_words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    return " ".join(filtered_words)


def analyze_sentiment(text):

    processed_text = preprocess_text(text)
    sentiment_score = sia.polarity_scores(processed_text)
    compound = sentiment_score['compound']
    
    # Condition for to check comments sentiment result 
    if compound > 0.05:
        return "positive", round(compound, 2)
    elif compound < -0.05:
        return "negative", round(compound, 2)
    else:
        return "neutral", round(compound, 2)
