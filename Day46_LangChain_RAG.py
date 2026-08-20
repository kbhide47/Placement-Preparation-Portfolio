# ==========================================================
# DAY 46 - LANGCHAIN + DOCUMENT LOADING + CHUNKING + RAG
# ==========================================================

import os

from dotenv import load_dotenv

from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_google_genai import ChatGoogleGenerativeAI


# ==========================================================
# Q1. What is LangChain?
# ==========================================================

# LangChain is a framework used to build applications
# around LLMs.
#
# It provides components for:
#
# - Prompts
# - LLMs
# - Document loaders
# - Text splitters
# - Embeddings
# - Retrievers
# - Vector stores
# - Chains
#
# It is especially useful for building RAG applications.


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
# Q3. Create LLM
# ==========================================================

llm = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash",

    google_api_key=API_KEY,

    temperature=0.2

)


# ==========================================================
# Q4. Create Sample Documents
# ==========================================================

documents = [

    Document(
        page_content="""
        Python is a high-level programming language.
        It is widely used for data analysis, machine
        learning, automation and artificial intelligence.
        """,

        metadata={
            "source": "python.txt"
        }
    ),

    Document(
        page_content="""
        Pandas is a Python library used for data
        manipulation and analysis. It provides
        DataFrame and Series data structures.
        """,

        metadata={
            "source": "pandas.txt"
        }
    ),

    Document(
        page_content="""
        Machine learning is a branch of artificial
        intelligence where algorithms learn patterns
        from data to make predictions.
        """,

        metadata={
            "source": "ml.txt"
        }
    ),

    Document(
        page_content="""
        RAG stands for Retrieval-Augmented Generation.
        It retrieves relevant information from an
        external knowledge source and gives that
        information to an LLM as context.
        """,

        metadata={
            "source": "rag.txt"
        }
    )

]


# ==========================================================
# Q5. Understand Document Object
# ==========================================================

for document in documents:

    print(
        "Content:",
        document.page_content
    )

    print(
        "Metadata:",
        document.metadata
    )

    print(
        "-" * 50
    )


# ==========================================================
# Q6. Create Text Splitter
# ==========================================================

text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=300,

    chunk_overlap=50

)


# ==========================================================
# Q7. Split Documents into Chunks
# ==========================================================

chunks = text_splitter.split_documents(
    documents
)


print(
    "Number of chunks:",
    len(chunks)
)


# ==========================================================
# Q8. Display Chunks
# ==========================================================

for i, chunk in enumerate(chunks):

    print(
        f"\nChunk {i + 1}:"
    )

    print(
        chunk.page_content
    )

    print(
        "Metadata:",
        chunk.metadata
    )


# ==========================================================
# Q9. What is Chunk Size?
# ==========================================================

# chunk_size determines approximately how much text
# each chunk should contain.
#
# Smaller chunks:
# - More precise retrieval
# - Less context
#
# Larger chunks:
# - More context
# - Potentially less precise retrieval


# ==========================================================
# Q10. What is Chunk Overlap?
# ==========================================================

# Chunk overlap keeps some text from the previous
# chunk in the next chunk.
#
# Example:
#
# Chunk 1:
# "Python is used for data analysis and machine learning"
#
# Chunk 2:
# "machine learning is also used for artificial intelligence"
#
# The overlapping portion helps preserve context.


# ==========================================================
# Q11. Create Embedding Model
# ==========================================================

embeddings = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)


# ==========================================================
# Q12. Create FAISS Vector Store
# ==========================================================

vector_store = FAISS.from_documents(

    chunks,

    embeddings

)


print(
    "Vector store created successfully."
)


# ==========================================================
# Q13. Create Retriever
# ==========================================================

retriever = vector_store.as_retriever(

    search_kwargs={
        "k": 2
    }

)


# ==========================================================
# Q14. Retrieve Relevant Documents
# ==========================================================

query = (
    "What is RAG?"
)


retrieved_docs = retriever.invoke(
    query
)


print(
    "\nRetrieved Documents:"
)


for document in retrieved_docs:

    print(
        document.page_content
    )

    print(
        "Source:",
        document.metadata.get(
            "source"
        )
    )

    print(
        "-" * 50
    )


# ==========================================================
# Q15. Build Context
# ==========================================================

context = "\n\n".join(

    document.page_content

    for document in retrieved_docs

)


# ==========================================================
# Q16. Create RAG Prompt
# ==========================================================

prompt = f"""
You are a helpful AI assistant.

Answer the question using only the
provided context.

If the answer is not present in the
context, say:

"Information not available in the
knowledge base."

Context:
{context}

Question:
{query}

Answer:
"""


# ==========================================================
# Q17. Generate Answer
# ==========================================================

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
# Q18. Create Reusable RAG Function
# ==========================================================

def ask_rag(question):

    retrieved_docs = retriever.invoke(
        question
    )

    context = "\n\n".join(

        document.page_content

        for document in retrieved_docs

    )

    prompt = f"""
    Answer the question using only the
    provided context.

    Context:
    {context}

    Question:
    {question}

    If the answer is unavailable,
    say "Information not available."

    Answer:
    """

    response = llm.invoke(
        prompt
    )

    return response.content


# ==========================================================
# Q19. Test Multiple Questions
# ==========================================================

questions = [

    "What is Python?",

    "What is Pandas?",

    "What is machine learning?",

    "What is RAG?",

    "What is LangChain?"

]


for question in questions:

    print(
        "\nQuestion:",
        question
    )

    print(
        "Answer:",
        ask_rag(question)
    )


# ==========================================================
# Q20. Complete LangChain RAG Architecture
# ==========================================================

print("""
                DOCUMENT INGESTION

Documents
    ↓
Document Loader
    ↓
Document Objects
    ↓
Text Splitter
    ↓
Chunks
    ↓
Embedding Model
    ↓
Vector Store


                USER QUERY

User Question
      ↓
Retriever
      ↓
Relevant Chunks
      ↓
Context
      ↓
Prompt
      ↓
LLM
      ↓
Final Answer
""")


# ==========================================================
# END OF DAY 46
# ==========================================================
