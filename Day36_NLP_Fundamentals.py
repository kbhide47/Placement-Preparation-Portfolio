# ==========================================================
# DAY 36 - NLP FUNDAMENTALS
# ==========================================================

# Install:
# pip install nltk scikit-learn pandas

import re
import pandas as pd

import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import (
    CountVectorizer,
    TfidfVectorizer
)


# ==========================================================
# Download NLTK Resources
# ==========================================================

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")


# ==========================================================
# Q1. Create Sample Text
# ==========================================================

text = """
Artificial Intelligence is transforming the world.
Machine learning helps computers learn from data.
Natural Language Processing helps computers understand text.
"""


print(text)


# ==========================================================
# Q2. Convert Text to Lowercase
# ==========================================================

lower_text = text.lower()

print(lower_text)


# ==========================================================
# Q3. Remove Special Characters
# ==========================================================

clean_text = re.sub(
    r"[^a-zA-Z\s]",
    "",
    lower_text
)

print(clean_text)


# ==========================================================
# Q4. Tokenization
# ==========================================================

tokens = word_tokenize(
    clean_text
)

print(tokens)


# ==========================================================
# Q5. Remove Stopwords
# ==========================================================

stop_words = set(
    stopwords.words("english")
)

filtered_words = [

    word

    for word in tokens

    if word not in stop_words

]

print(filtered_words)


# ==========================================================
# Q6. Stemming
# ==========================================================

stemmer = PorterStemmer()

stemmed_words = [

    stemmer.stem(word)

    for word in filtered_words

]

print(stemmed_words)


# ==========================================================
# Q7. Lemmatization
# ==========================================================

lemmatizer = WordNetLemmatizer()

lemmatized_words = [

    lemmatizer.lemmatize(word)

    for word in filtered_words

]

print(lemmatized_words)


# ==========================================================
# Q8. Create Small Text Dataset
# ==========================================================

documents = [

    "I love machine learning",

    "Machine learning is interesting",

    "I love artificial intelligence",

    "Artificial intelligence is powerful"

]


# ==========================================================
# Q9. Bag of Words
# ==========================================================

bow = CountVectorizer()

bow_matrix = bow.fit_transform(
    documents
)

print(
    "Vocabulary:"
)

print(
    bow.get_feature_names_out()
)

print(
    "Bag of Words:"
)

print(
    bow_matrix.toarray()
)


# ==========================================================
# Q10. TF-IDF
# ==========================================================

tfidf = TfidfVectorizer()

tfidf_matrix = tfidf.fit_transform(
    documents
)

print(
    "TF-IDF Vocabulary:"
)

print(
    tfidf.get_feature_names_out()
)

print(
    "TF-IDF Matrix:"
)

print(
    tfidf_matrix.toarray()
)


# ==========================================================
# Q11. Create Bigrams
# ==========================================================

bigram_vectorizer = CountVectorizer(
    ngram_range=(2, 2)
)

bigram_matrix = bigram_vectorizer.fit_transform(
    documents
)

print(
    "Bigrams:"
)

print(
    bigram_vectorizer.get_feature_names_out()
)


# ==========================================================
# Q12. Create Unigrams + Bigrams
# ==========================================================

ngram_vectorizer = CountVectorizer(
    ngram_range=(1, 2)
)

ngram_matrix = ngram_vectorizer.fit_transform(
    documents
)

print(
    "Unigrams + Bigrams:"
)

print(
    ngram_vectorizer.get_feature_names_out()
)


# ==========================================================
# Q13. Transform New Text using TF-IDF
# ==========================================================

new_text = [

    "machine learning is powerful"

]

new_vector = tfidf.transform(
    new_text
)

print(
    "New Text TF-IDF:"
)

print(
    new_vector.toarray()
)


# ==========================================================
# Q14. Create Simple Text Classification Dataset
# ==========================================================

data = {

    "text": [

        "I love this product",

        "This product is excellent",

        "Very good experience",

        "I hate this product",

        "This product is terrible",

        "Very bad experience"

    ],

    "label": [

        1,
        1,
        1,
        0,
        0,
        0

    ]

}

df = pd.DataFrame(data)

print(df)


# ==========================================================
# Q15. Convert Text into TF-IDF Features
# ==========================================================

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(
    df["text"]
)

y = df["label"]

print(
    "Feature Matrix Shape:",
    X.shape
)


# ==========================================================
# Q16. Display TF-IDF Features
# ==========================================================

print(
    vectorizer.get_feature_names_out()
)


# ==========================================================
# Q17. Understand Sparse Matrix
# ==========================================================

print(
    "Sparse Matrix:"
)

print(X)


# ==========================================================
# Q18. Convert Sparse Matrix to Array
# ==========================================================

print(
    X.toarray()
)


# ==========================================================
# Q19. Transform New Sentence
# ==========================================================

new_sentence = [

    "excellent product"

]

new_features = vectorizer.transform(
    new_sentence
)

print(
    "New Sentence Features:"
)

print(
    new_features.toarray()
)


# ==========================================================
# Q20. Final NLP Pipeline
# ==========================================================

print("""
NLP WORKFLOW

Raw Text
   ↓
Lowercase
   ↓
Remove Noise
   ↓
Tokenization
   ↓
Stopword Removal
   ↓
Stemming / Lemmatization
   ↓
Vectorization
   ↓
Machine Learning Model
   ↓
Prediction
""")


# ==========================================================
# END OF DAY 36
# ==========================================================
