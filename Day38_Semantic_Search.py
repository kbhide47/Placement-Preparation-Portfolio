# ==========================================================
# DAY 38 - SENTENCE EMBEDDINGS + SEMANTIC SEARCH
# ==========================================================

# Install:
#
# pip install sentence-transformers scikit-learn numpy


import numpy as np

from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity


# ==========================================================
# Q1. Load a Pretrained Sentence Embedding Model
# ==========================================================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print(
    "Embedding model loaded successfully!"
)


# ==========================================================
# Q2. Create Sample Sentences
# ==========================================================

sentences = [

    "Machine learning is a branch of artificial intelligence.",

    "Artificial intelligence allows computers to learn from data.",

    "Python is commonly used for machine learning.",

    "I enjoy eating pizza and pasta.",

    "The weather is very pleasant today.",

    "Deep learning uses neural networks."

]


print(sentences)


# ==========================================================
# Q3. Generate Sentence Embeddings
# ==========================================================

embeddings = model.encode(
    sentences
)


print(
    "Embedding Shape:",
    embeddings.shape
)


# ==========================================================
# Q4. Check One Sentence Embedding
# ==========================================================

print(
    "First Sentence Embedding:"
)

print(
    embeddings[0]
)


# ==========================================================
# Q5. Understand Embedding Dimensions
# ==========================================================

print(
    "Number of dimensions:",
    embeddings.shape[1]
)


# ==========================================================
# Q6. Calculate Similarity Between Two Sentences
# ==========================================================

similarity = cosine_similarity(

    [embeddings[0]],

    [embeddings[1]]

)


print(
    "Similarity:",
    similarity[0][0]
)


# ==========================================================
# Q7. Compare Machine Learning and Pizza
# ==========================================================

similarity = cosine_similarity(

    [embeddings[0]],

    [embeddings[3]]

)


print(
    "ML vs Pizza Similarity:",
    similarity[0][0]
)


# ==========================================================
# Q8. Create a User Query
# ==========================================================

query = (
    "What is artificial intelligence?"
)


# ==========================================================
# Q9. Convert Query into Embedding
# ==========================================================

query_embedding = model.encode(
    [query]
)


print(
    "Query Embedding Shape:",
    query_embedding.shape
)


# ==========================================================
# Q10. Calculate Query Similarity with Documents
# ==========================================================

similarities = cosine_similarity(

    query_embedding,

    embeddings

)[0]


print(
    "Similarity Scores:"
)

print(
    similarities
)


# ==========================================================
# Q11. Rank Documents by Similarity
# ==========================================================

ranked_indices = np.argsort(
    similarities
)[::-1]


print(
    "Ranked Document Indices:"
)

print(
    ranked_indices
)


# ==========================================================
# Q12. Display Ranked Results
# ==========================================================

print(
    "\nSemantic Search Results:\n"
)

for index in ranked_indices:

    print(
        "Score:",
        round(
            similarities[index],
            4
        )
    )

    print(
        "Text:",
        sentences[index]
    )

    print(
        "-" * 50
    )


# ==========================================================
# Q13. Retrieve Top 3 Results
# ==========================================================

top_k = 3

top_indices = ranked_indices[:top_k]


print(
    "\nTop 3 Results:"
)

for index in top_indices:

    print(
        sentences[index]
    )


# ==========================================================
# Q14. Create a Small Knowledge Base
# ==========================================================

documents = [

    "Python is a programming language used for data science.",

    "Pandas is a Python library used for data manipulation.",

    "NumPy provides numerical computing functionality.",

    "Machine learning models learn patterns from data.",

    "Deep learning uses neural networks with multiple layers.",

    "RAG combines retrieval with large language models.",

    "Vector databases store and search embeddings.",

    "FastAPI can be used to create APIs in Python."

]


# ==========================================================
# Q15. Generate Document Embeddings
# ==========================================================

document_embeddings = model.encode(
    documents
)


print(
    "Document Embedding Shape:",
    document_embeddings.shape
)


# ==========================================================
# Q16. Create a RAG-Style Query
# ==========================================================

query = (
    "How can I search information using vectors?"
)


# ==========================================================
# Q17. Generate Query Embedding
# ==========================================================

query_embedding = model.encode(
    [query]
)


# ==========================================================
# Q18. Semantic Search
# ==========================================================

scores = cosine_similarity(

    query_embedding,

    document_embeddings

)[0]


# ==========================================================
# Q19. Get Top 3 Relevant Documents
# ==========================================================

top_indices = np.argsort(
    scores
)[::-1][:3]


print(
    "\nTop Relevant Documents:\n"
)

for index in top_indices:

    print(
        "Score:",
        round(
            scores[index],
            4
        )
    )

    print(
        "Document:",
        documents[index]
    )

    print(
        "-" * 60
    )


# ==========================================================
# Q20. Understand the RAG Retrieval Process
# ==========================================================

print("""
RAG RETRIEVAL PROCESS

Documents
    ↓
Split into chunks
    ↓
Generate embeddings
    ↓
Store embeddings
    ↓
User Query
    ↓
Generate query embedding
    ↓
Cosine Similarity Search
    ↓
Retrieve Top-K Documents
    ↓
Send retrieved context to LLM
    ↓
Generate final answer
""")


# ==========================================================
# END OF DAY 38
# ==========================================================
