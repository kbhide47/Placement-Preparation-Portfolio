# ==========================================================
# DAY 47 - ADVANCED RAG
# ==========================================================

import os

from dotenv import load_dotenv

from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_google_genai import ChatGoogleGenerativeAI


# ==========================================================
# Q1. What is Advanced RAG?
# ==========================================================

# Advanced RAG improves the basic RAG pipeline
# to increase retrieval quality and answer accuracy.
#
# Basic RAG:
#
# Query
#   ↓
# Retrieval
#   ↓
# LLM
#
# Advanced RAG may include:
#
# Query transformation
# Better retrieval
# Metadata filtering
# Reranking
# Context filtering
# Evaluation


# ==========================================================
# Q2. Load API Key
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
# Q3. Create LLM
# ==========================================================

llm = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash",

    google_api_key=API_KEY,

    temperature=0.2

)


# ==========================================================
# Q4. Create Knowledge Base
# ==========================================================

documents = [

    Document(
        page_content="""
        Python is a high-level programming language
        commonly used in data analysis, machine learning,
        automation and artificial intelligence.
        """,
        metadata={
            "topic": "python",
            "source": "python.txt"
        }
    ),

    Document(
        page_content="""
        Pandas provides DataFrame and Series data
        structures for data manipulation, cleaning,
        filtering, grouping and analysis.
        """,
        metadata={
            "topic": "pandas",
            "source": "pandas.txt"
        }
    ),

    Document(
        page_content="""
        NumPy provides multidimensional arrays and
        numerical computing functionality in Python.
        """,
        metadata={
            "topic": "numpy",
            "source": "numpy.txt"
        }
    ),

    Document(
        page_content="""
        Machine learning algorithms learn patterns
        from data and use those patterns to make
        predictions or decisions.
        """,
        metadata={
            "topic": "machine_learning",
            "source": "ml.txt"
        }
    ),

    Document(
        page_content="""
        RAG combines retrieval with generation.
        Relevant documents are retrieved from an
        external knowledge source and provided to
        an LLM as context.
        """,
        metadata={
            "topic": "rag",
            "source": "rag.txt"
        }
    ),

    Document(
        page_content="""
        FAISS is a library for efficient similarity
        search over dense vectors. It can be used
        as a local vector store in RAG applications.
        """,
        metadata={
            "topic": "vector_database",
            "source": "faiss.txt"
        }
    )

]


# ==========================================================
# Q5. Split Documents
# ==========================================================

splitter = RecursiveCharacterTextSplitter(

    chunk_size=250,

    chunk_overlap=50

)

chunks = splitter.split_documents(
    documents
)


print(
    "Number of chunks:",
    len(chunks)
)


# ==========================================================
# Q6. Create Embeddings
# ==========================================================

embeddings = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)


# ==========================================================
# Q7. Create Vector Store
# ==========================================================

vector_store = FAISS.from_documents(

    chunks,

    embeddings

)


# ==========================================================
# Q8. Similarity Search
# ==========================================================

query = (
    "What is used for data analysis in Python?"
)


results = vector_store.similarity_search(

    query,

    k=3

)


print(
    "\nSimilarity Search Results:"
)


for result in results:

    print(
        result.page_content
    )

    print(
        "Metadata:",
        result.metadata
    )

    print(
        "-" * 50
    )


# ==========================================================
# Q9. What is Top-K?
# ==========================================================

# k determines how many relevant documents/chunks
# are returned.
#
# k = 3
#
# means retrieve the top 3 results.


results = vector_store.similarity_search(

    query,

    k=3

)

print(
    "Retrieved documents:",
    len(results)
)


# ==========================================================
# Q10. Similarity Search with Scores
# ==========================================================

results_with_scores = (
    vector_store.similarity_search_with_score(
        query,
        k=3
    )
)


for document, score in results_with_scores:

    print(
        "\nDocument:"
    )

    print(
        document.page_content
    )

    print(
        "Score:",
        score
    )


# ==========================================================
# Q11. Understand Similarity Score
# ==========================================================

# Similarity search measures how closely the query
# matches stored vectors.
#
# IMPORTANT:
#
# The exact meaning and direction of a score depends
# on the similarity/distance metric used.
#
# For FAISS IndexFlatL2, a smaller distance generally
# means the vectors are closer.


# ==========================================================
# Q12. Metadata Filtering
# ==========================================================

filtered_results = (
    vector_store.similarity_search(
        query,
        k=3,
        filter={
            "topic": "python"
        }
    )
)


print(
    "\nMetadata Filter Results:"
)


for document in filtered_results:

    print(
        document.page_content
    )

    print(
        document.metadata
    )


# ==========================================================
# Q13. Why Metadata?
# ==========================================================

# Metadata can contain information such as:
#
# source
# topic
# date
# department
# document type
# user
#
# It can help restrict retrieval to relevant documents.


# ==========================================================
# Q14. Create a Retriever
# ==========================================================

retriever = vector_store.as_retriever(

    search_kwargs={
        "k": 3
    }

)


retrieved_docs = retriever.invoke(
    query
)


print(
    "\nRetriever Results:"
)


for document in retrieved_docs:

    print(
        document.page_content
    )


# ==========================================================
# Q15. Query Transformation
# ==========================================================

# A user query may be vague.
#
# Example:
#
# "How does it work?"
#
# A query transformation step can rewrite the
# question into a more useful search query.


original_query = (
    "How does it work?"
)


rewrite_prompt = f"""
Rewrite the following question into a clear
search query.

Question:
{original_query}

Return only the rewritten query.
"""


rewritten_query = llm.invoke(
    rewrite_prompt
)


print(
    "\nRewritten Query:"
)

print(
    rewritten_query.content
)


# ==========================================================
# Q16. Multi-Query Retrieval
# ==========================================================

# One query may not capture all relevant information.
#
# Multi-query retrieval generates multiple versions
# of the user's question and retrieves documents
# for each version.


user_query = (
    "Explain RAG."
)


multi_query_prompt = f"""
Generate 3 different search queries for:

{user_query}

Return one query per line.
"""


multi_query_response = llm.invoke(
    multi_query_prompt
)


print(
    "\nGenerated Search Queries:"
)

print(
    multi_query_response.content
)


# ==========================================================
# Q17. Context Filtering
# ==========================================================

# Retrieval may return irrelevant chunks.
#
# Before sending retrieved information to the LLM,
# we can remove irrelevant content.


query = (
    "What is RAG?"
)


retrieved_docs = retriever.invoke(
    query
)


context = "\n\n".join(

    doc.page_content

    for doc in retrieved_docs

)


print(
    "\nRetrieved Context:"
)

print(
    context
)


# ==========================================================
# Q18. Generate Grounded Answer
# ==========================================================

prompt = f"""
Answer the question using ONLY the context.

Context:
{context}

Question:
{query}

If the answer is not available in the context,
say:

"Information not available in the knowledge base."

Answer:
"""


response = llm.invoke(
    prompt
)


print(
    "\nFinal Answer:"
)

print(
    response.content
)


# ==========================================================
# Q19. Handle "Answer Not Found"
# ==========================================================

unknown_query = (
    "What is the population of Mars?"
)


retrieved_docs = retriever.invoke(
    unknown_query
)


context = "\n\n".join(

    doc.page_content

    for doc in retrieved_docs

)


prompt = f"""
Answer the question using ONLY the context.

Context:
{context}

Question:
{unknown_query}

If the answer is not supported by the context,
say:

"Information not available."
"""


response = llm.invoke(
    prompt
)


print(
    "\nUnknown Question Answer:"
)

print(
    response.content
)


# ==========================================================
# Q20. Advanced RAG Architecture
# ==========================================================

print("""
ADVANCED RAG

Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
User Query
    ↓
Query Transformation
    ↓
Retriever
    ↓
Top-K Retrieval
    ↓
Metadata Filtering
    ↓
Reranking / Relevance Filtering
    ↓
Relevant Context
    ↓
LLM
    ↓
Grounded Answer
    ↓
Evaluation
""")


# ==========================================================
# END OF DAY 47
# ==========================================================
