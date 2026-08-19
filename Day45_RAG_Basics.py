# ==========================================================
# DAY 45 - RAG FUNDAMENTALS + BASIC RAG SYSTEM
# ==========================================================

import os

import numpy as np

import faiss

from dotenv import load_dotenv

from sentence_transformers import SentenceTransformer

from google import genai


# ==========================================================
# Q1. What is RAG?
# ==========================================================

# RAG = Retrieval-Augmented Generation.
#
# RAG combines:
#
# 1. Information retrieval
# 2. Large Language Model generation
#
# Instead of asking the LLM to answer only from
# its internal knowledge, we retrieve relevant
# information and provide it as context.


# ==========================================================
# Q2. Load Environment Variables
# ==========================================================

load_dotenv()


API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


if not API_KEY:

    raise ValueError(
        "GEMINI_API_KEY is not set."
    )


# ==========================================================
# Q3. Create LLM Client
# ==========================================================

client = genai.Client(
    api_key=API_KEY
)


# ==========================================================
# Q4. Create Sample Knowledge Base
# ==========================================================

documents = [

    """
    Python is a high-level programming language.
    It is widely used for data analysis, machine learning,
    automation, web development and artificial intelligence.
    """,

    """
    Pandas is a Python library used for data manipulation
    and analysis. It provides DataFrame and Series data
    structures and supports filtering, grouping and
    handling missing values.
    """,

    """
    NumPy is a Python library for numerical computing.
    It provides arrays, mathematical operations and
    efficient numerical processing.
    """,

    """
    Machine learning is a field of artificial intelligence
    where algorithms learn patterns from data and use
    those patterns to make predictions or decisions.
    """,

    """
    RAG stands for Retrieval-Augmented Generation.
    It retrieves relevant information from an external
    knowledge source and provides that information to
    a language model as context.
    """,

    """
    A vector database stores numerical vector
    representations called embeddings and allows
    similarity search over those vectors.
    """

]


# ==========================================================
# Q5. Create Embedding Model
# ==========================================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ==========================================================
# Q6. Convert Documents into Embeddings
# ==========================================================

document_embeddings = embedding_model.encode(
    documents
)


print(
    "Embedding Shape:",
    document_embeddings.shape
)


# ==========================================================
# Q7. Understand Embedding Dimension
# ==========================================================

embedding_dimension = (
    document_embeddings.shape[1]
)


print(
    "Embedding Dimension:",
    embedding_dimension
)


# ==========================================================
# Q8. Create FAISS Vector Index
# ==========================================================

index = faiss.IndexFlatL2(
    embedding_dimension
)


# ==========================================================
# Q9. Add Document Embeddings to FAISS
# ==========================================================

index.add(
    np.array(
        document_embeddings
    ).astype("float32")
)


print(
    "Number of vectors:",
    index.ntotal
)


# ==========================================================
# Q10. Create User Query
# ==========================================================

query = (
    "What is a vector database?"
)


# ==========================================================
# Q11. Convert Query into Embedding
# ==========================================================

query_embedding = embedding_model.encode(
    [query]
)


query_embedding = np.array(
    query_embedding
).astype("float32")


# ==========================================================
# Q12. Perform Similarity Search
# ==========================================================

distances, indices = index.search(
    query_embedding,
    2
)


print(
    "Retrieved indices:"
)

print(
    indices
)


# ==========================================================
# Q13. Retrieve Relevant Documents
# ==========================================================

retrieved_documents = [

    documents[index_id]

    for index_id in indices[0]

]


print(
    "\nRetrieved Documents:"
)

for document in retrieved_documents:

    print(
        document
    )

    print(
        "-" * 50
    )


# ==========================================================
# Q14. Combine Retrieved Documents
# ==========================================================

context = "\n\n".join(
    retrieved_documents
)


print(
    "Context:"
)

print(
    context
)


# ==========================================================
# Q15. Create RAG Prompt
# ==========================================================

prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY
the provided context.

If the answer is not present in the context,
say that the information is not available.

Context:
{context}

Question:
{query}

Answer:
"""


# ==========================================================
# Q16. Send Context + Question to LLM
# ==========================================================

response = client.models.generate_content(

    model="gemini-2.5-flash",

    contents=prompt

)


# ==========================================================
# Q17. Display Final Answer
# ==========================================================

print(
    "\nFinal Answer:"
)

print(
    response.text
)


# ==========================================================
# Q18. Create Reusable RAG Function
# ==========================================================

def rag(query, top_k=2):

    # Convert query to embedding

    query_embedding = embedding_model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")


    # Retrieve relevant documents

    distances, indices = index.search(
        query_embedding,
        top_k
    )


    # Get documents

    retrieved_documents = [

        documents[i]

        for i in indices[0]

    ]


    # Build context

    context = "\n\n".join(
        retrieved_documents
    )


    # Build prompt

    prompt = f"""
    Answer the question using only the
    context below.

    Context:
    {context}

    Question:
    {query}

    If the answer is not available,
    say "Information not available."

    Answer:
    """


    # Call LLM

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=prompt

    )


    return response.text


# ==========================================================
# Q19. Test RAG System
# ==========================================================

questions = [

    "What is Pandas?",

    "What is machine learning?",

    "What is RAG?",

    "What is NumPy?",

    "What is a vector database?"

]


for question in questions:

    print(
        "\nQuestion:",
        question
    )

    answer = rag(
        question
    )

    print(
        "Answer:",
        answer
    )


# ==========================================================
# Q20. Complete RAG Architecture
# ==========================================================

print("""
RAG ARCHITECTURE

Documents
    ↓
Document Loading
    ↓
Chunking
    ↓
Embedding Model
    ↓
Vector Embeddings
    ↓
Vector Database
    ↓
        User Query
             ↓
      Query Embedding
             ↓
      Similarity Search
             ↓
       Top-K Chunks
             ↓
          Context
             ↓
      Prompt + Context
             ↓
            LLM
             ↓
       Final Answer
""")


# ==========================================================
# END OF DAY 45
# ==========================================================
