# ==========================================================
# DAY 19 - LLM, EMBEDDINGS, FAISS & RAG
#
# Topics:
# 1. What is an LLM?
# 2. Sentence Embeddings
# 3. Vector Embeddings
# 4. Cosine Similarity
# 5. FAISS Vector Database
# 6. Semantic Search
# 7. Simple RAG Pipeline
# ==========================================================

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# ---------------------------------------------------------

print("="*60)
print("Question 1 : Load Embedding Model")
print("="*60)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Embedding Model Loaded Successfully")

# ---------------------------------------------------------

print("\nQuestion 2 : Documents")

documents = [

    "Python is a programming language.",

    "Machine Learning is used for prediction.",

    "Artificial Intelligence mimics human intelligence.",

    "RAG combines retrieval with language models.",

    "FAISS stores vector embeddings efficiently."

]

print(documents)

# ---------------------------------------------------------

print("\nQuestion 3 : Create Embeddings")

embeddings = model.encode(documents)

print("Embedding Shape:")

print(embeddings.shape)

# ---------------------------------------------------------

print("\nQuestion 4 : Create FAISS Index")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

print("Total Documents:", index.ntotal)

# ---------------------------------------------------------

print("\nQuestion 5 : User Query")

query = "What is RAG?"

query_embedding = model.encode([query])

# ---------------------------------------------------------

print("\nQuestion 6 : Search Similar Documents")

distance, indices = index.search(
    np.array(query_embedding),
    k=2
)

print("Nearest Documents:")

for i in indices[0]:

    print(documents[i])

# ---------------------------------------------------------

print("\nQuestion 7 : Cosine Similarity")

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(
    query_embedding,
    embeddings
)

print(similarity)

# ---------------------------------------------------------

print("\nQuestion 8 : Best Match")

best = np.argmax(similarity)

print("Best Document:")

print(documents[best])

# ---------------------------------------------------------

print("\nQuestion 9 : Simple RAG")

retrieved_context = documents[best]

print("Retrieved Context:")

print(retrieved_context)

print("\nLLM Prompt")

prompt = f"""

Answer the question using the context.

Context:

{retrieved_context}

Question:

{query}

"""

print(prompt)

# ---------------------------------------------------------

print("\nQuestion 10 : Embedding Dimension")

print(embeddings.shape[1])

print("\nDay 19 Completed Successfully!")
