import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

english_stopwords = set(
    stopwords.words('english')
)

# Simple Amharic stopwords
amharic_stopwords = {

    "እና",
    "ነው",
    "የ",
    "በ",
    "ለ",
    "ነበር"
}

def normalize_amharic(text):

    text = text.replace("ሃ", "ሀ")
    text = text.replace("ኅ", "ህ")
    text = text.replace("ጸ", "ፀ")

    return text


def preprocess_text(text):

    text = text.lower()

    # Amharic normalization
    text = normalize_amharic(text)

    tokens = word_tokenize(text)

    tokens = [

        word for word in tokens

        if word not in english_stopwords
        and word not in amharic_stopwords
        and word not in string.punctuation
    ]

    return tokens