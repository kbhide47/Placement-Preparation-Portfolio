# ==========================================================
# DAY 18 - NATURAL LANGUAGE PROCESSING (NLP)
#
# Topics:
# 1. Text Cleaning
# 2. Lowercase Conversion
# 3. Remove Punctuation
# 4. Tokenization
# 5. Stopwords Removal
# 6. Stemming
# 7. Lemmatization
# 8. Bag of Words
# 9. TF-IDF
# 10. Mini Sentiment Prediction
# ==========================================================

import re
import string
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Download required resources (run once)
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")

# ---------------------------------------------------------

print("=" * 60)
print("Question 1 : Original Text")
print("=" * 60)

text = "I love Machine Learning! It is amazing and very useful."

print(text)

# ---------------------------------------------------------

print("\nQuestion 2 : Convert to Lowercase")

text = text.lower()

print(text)

# ---------------------------------------------------------

print("\nQuestion 3 : Remove Punctuation")

text = text.translate(str.maketrans("", "", string.punctuation))

print(text)

# ---------------------------------------------------------

print("\nQuestion 4 : Remove Numbers")

sample = "Python 3.12 is awesome 100%"

clean = re.sub(r"\d+", "", sample)

print(clean)

# ---------------------------------------------------------

print("\nQuestion 5 : Tokenization")

tokens = word_tokenize(text)

print(tokens)

# ---------------------------------------------------------

print("\nQuestion 6 : Remove Stopwords")

stop_words = set(stopwords.words("english"))

filtered = [
    word
    for word in tokens
    if word not in stop_words
]

print(filtered)

# ---------------------------------------------------------

print("\nQuestion 7 : Stemming")

stemmer = PorterStemmer()

stemmed = [
    stemmer.stem(word)
    for word in filtered
]

print(stemmed)

# ---------------------------------------------------------

print("\nQuestion 8 : Lemmatization")

lemmatizer = WordNetLemmatizer()

lemmatized = [
    lemmatizer.lemmatize(word)
    for word in filtered
]

print(lemmatized)

# ---------------------------------------------------------

print("\nQuestion 9 : Bag of Words")

documents = [

    "Machine learning is amazing",

    "I love Python",

    "Python is used for AI",

    "Machine learning uses data"

]

vectorizer = CountVectorizer()

bow = vectorizer.fit_transform(documents)

print("Vocabulary:")

print(vectorizer.get_feature_names_out())

print("\nBag of Words Matrix")

print(bow.toarray())

# ---------------------------------------------------------

print("\nQuestion 10 : TF-IDF")

tfidf = TfidfVectorizer()

matrix = tfidf.fit_transform(documents)

print(tfidf.get_feature_names_out())

print(matrix.toarray())

# ---------------------------------------------------------

print("\nQuestion 11 : Mini Sentiment Prediction")

sentence = "I really love AI"

positive_words = ["love", "good", "excellent", "great", "amazing"]

negative_words = ["bad", "hate", "poor", "worst"]

tokens = sentence.lower().split()

score = 0

for word in tokens:

    if word in positive_words:

        score += 1

    elif word in negative_words:

        score -= 1

if score > 0:

    print("Positive Sentiment")

elif score < 0:

    print("Negative Sentiment")

else:

    print("Neutral Sentiment")

# ---------------------------------------------------------

print("\nQuestion 12 : Most Important NLP Steps")

print("""
1. Text Cleaning
2. Tokenization
3. Stopword Removal
4. Stemming
5. Lemmatization
6. Vectorization
7. Model Training
""")

# ---------------------------------------------------------

print("\nDay 18 Completed Successfully!")
