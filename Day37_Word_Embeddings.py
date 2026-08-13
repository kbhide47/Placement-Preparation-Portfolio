# ==========================================================
# DAY 37 - WORD EMBEDDINGS
# ==========================================================

# Install:
#
# pip install gensim scikit-learn numpy


import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from gensim.models import Word2Vec


# ==========================================================
# Q1. What is a Word Embedding?
# ==========================================================

# A word embedding represents a word as a numerical vector.
#
# Example:
#
# "king"   -> [0.21, 0.53, 0.12, ...]
# "queen"  -> [0.19, 0.50, 0.15, ...]
#
# Similar words tend to have similar vector representations.


# ==========================================================
# Q2. Create Sample Sentences
# ==========================================================

sentences = [

    ["machine", "learning", "is", "powerful"],

    ["machine", "learning", "uses", "data"],

    ["deep", "learning", "uses", "neural", "networks"],

    ["artificial", "intelligence", "uses", "machine", "learning"],

    ["data", "science", "uses", "machine", "learning"],

    ["neural", "networks", "are", "used", "in", "deep", "learning"]

]


print(sentences)


# ==========================================================
# Q3. Train Word2Vec Model
# ==========================================================

model = Word2Vec(

    sentences=sentences,

    vector_size=50,

    window=3,

    min_count=1,

    workers=1,

    seed=42

)


print("Word2Vec model trained successfully!")


# ==========================================================
# Q4. Get Vocabulary
# ==========================================================

vocabulary = model.wv.index_to_key

print("Vocabulary:")

print(vocabulary)


# ==========================================================
# Q5. Get Vector for a Word
# ==========================================================

word_vector = model.wv["machine"]

print(
    "Machine Vector:"
)

print(word_vector)


# ==========================================================
# Q6. Check Vector Dimensions
# ==========================================================

print(
    "Vector Shape:",
    word_vector.shape
)


# ==========================================================
# Q7. Find Similar Words
# ==========================================================

similar_words = model.wv.most_similar(
    "learning",
    topn=3
)

print(
    "Words Similar to Learning:"
)

print(similar_words)


# ==========================================================
# Q8. Find Similarity Between Two Words
# ==========================================================

similarity = model.wv.similarity(
    "machine",
    "learning"
)

print(
    "Machine vs Learning Similarity:",
    similarity
)


# ==========================================================
# Q9. Calculate Cosine Similarity Manually
# ==========================================================

vector1 = model.wv["machine"]

vector2 = model.wv["learning"]


cosine = np.dot(vector1, vector2) / (

    np.linalg.norm(vector1)
    *
    np.linalg.norm(vector2)

)


print(
    "Cosine Similarity:",
    cosine
)


# ==========================================================
# Q10. Use sklearn Cosine Similarity
# ==========================================================

similarity_matrix = cosine_similarity(

    [vector1],

    [vector2]

)

print(
    "Sklearn Cosine Similarity:"
)

print(
    similarity_matrix
)


# ==========================================================
# Q11. Compare Two Similar Concepts
# ==========================================================

machine_vector = model.wv["machine"]

data_vector = model.wv["data"]


print(
    "Machine vs Data:"
)

print(
    model.wv.similarity(
        "machine",
        "data"
    )
)


# ==========================================================
# Q12. Find Most Similar Words to "data"
# ==========================================================

print(
    model.wv.most_similar(
        "data",
        topn=5
    )
)


# ==========================================================
# Q13. Check Whether a Word Exists
# ==========================================================

word = "python"

if word in model.wv:

    print(
        word,
        "exists in vocabulary"
    )

else:

    print(
        word,
        "does not exist in vocabulary"
    )


# ==========================================================
# Q14. Word Vector Arithmetic
# ==========================================================

# Word embeddings can sometimes capture relationships
# between concepts.
#
# Example from large pretrained models:
#
# king - man + woman ≈ queen
#
# Our tiny dataset is not large enough to reproduce
# meaningful relationships reliably.


# ==========================================================
# Q15. Save Word2Vec Model
# ==========================================================

model.save(
    "word2vec_model.model"
)

print(
    "Word2Vec model saved!"
)


# ==========================================================
# Q16. Load Word2Vec Model
# ==========================================================

loaded_model = Word2Vec.load(
    "word2vec_model.model"
)


print(
    "Model loaded successfully!"
)


# ==========================================================
# Q17. Get Vector from Loaded Model
# ==========================================================

loaded_vector = loaded_model.wv[
    "machine"
]

print(
    loaded_vector
)


# ==========================================================
# Q18. Sentence Embedding - Simple Average
# ==========================================================

sentence = [

    "machine",
    "learning",
    "uses",
    "data"

]


vectors = [

    model.wv[word]

    for word in sentence

    if word in model.wv

]


sentence_vector = np.mean(
    vectors,
    axis=0
)


print(
    "Sentence Vector:"
)

print(
    sentence_vector
)


# ==========================================================
# Q19. Compare Two Sentences
# ==========================================================

sentence1 = [
    "machine",
    "learning",
    "uses",
    "data"
]

sentence2 = [
    "artificial",
    "intelligence",
    "uses",
    "machine",
    "learning"
]


vector1 = np.mean(
    [
        model.wv[word]
        for word in sentence1
        if word in model.wv
    ],
    axis=0
)


vector2 = np.mean(
    [
        model.wv[word]
        for word in sentence2
        if word in model.wv
    ],
    axis=0
)


sentence_similarity = cosine_similarity(

    [vector1],

    [vector2]

)


print(
    "Sentence Similarity:"
)

print(
    sentence_similarity
)


# ==========================================================
# Q20. Understand Embeddings in RAG
# ==========================================================

print("""
RAG EMBEDDING WORKFLOW

Documents
    ↓
Text Chunks
    ↓
Embedding Model
    ↓
Numerical Vectors
    ↓
Vector Database
    ↓
User Question
    ↓
Question Embedding
    ↓
Similarity Search
    ↓
Relevant Documents
    ↓
LLM
    ↓
Answer
""")


# ==========================================================
# END OF DAY 37
# ==========================================================
