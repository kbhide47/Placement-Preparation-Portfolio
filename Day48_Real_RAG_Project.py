# ==========================================================
# DAY 48 - REAL RAG PROJECT
# AI DOCUMENT Q&A SYSTEM
# ==========================================================


# ==========================================================
# PART 1 - IMPORT LIBRARIES
# ==========================================================

import os

import streamlit as st

from dotenv import load_dotenv

from langchain_core.documents import Document

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import FAISS

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)


# ==========================================================
# PART 2 - LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv()

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


if not API_KEY:

    st.error(
        "GEMINI_API_KEY is not configured."
    )

    st.stop()


# ==========================================================
# PART 3 - CREATE LLM
# ==========================================================

llm = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash",

    google_api_key=API_KEY,

    temperature=0.2

)


# ==========================================================
# PART 4 - CREATE EMBEDDING MODEL
# ==========================================================

embeddings = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)


# ==========================================================
# PART 5 - LOAD KNOWLEDGE BASE
# ==========================================================

def load_documents():

    file_path = (
        "data/knowledge_base.txt"
    )

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()


    document = Document(

        page_content=text,

        metadata={
            "source": "knowledge_base.txt"
        }

    )

    return [document]


# ==========================================================
# PART 6 - CHUNK DOCUMENT
# ==========================================================

def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=100

    )

    chunks = splitter.split_documents(
        documents
    )

    return chunks


# ==========================================================
# PART 7 - CREATE VECTOR DATABASE
# ==========================================================

@st.cache_resource
def create_vector_store():

    documents = load_documents()

    chunks = create_chunks(
        documents
    )

    vector_store = FAISS.from_documents(

        chunks,

        embeddings

    )

    return vector_store


# ==========================================================
# PART 8 - CREATE RETRIEVER
# ==========================================================

vector_store = create_vector_store()


retriever = vector_store.as_retriever(

    search_kwargs={
        "k": 3
    }

)


# ==========================================================
# PART 9 - RETRIEVE DOCUMENTS
# ==========================================================

def retrieve_documents(query):

    documents = retriever.invoke(
        query
    )

    return documents


# ==========================================================
# PART 10 - BUILD CONTEXT
# ==========================================================

def create_context(documents):

    context = "\n\n".join(

        document.page_content

        for document in documents

    )

    return context


# ==========================================================
# PART 11 - GENERATE ANSWER
# ==========================================================

def generate_answer(
    question,
    context
):

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY
the information provided in the context.

Do not invent information.

If the answer cannot be found in the
context, say:

"Information not available in the
knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""


    response = llm.invoke(
        prompt
    )

    return response.content


# ==========================================================
# PART 12 - MAIN RAG FUNCTION
# ==========================================================

def rag_pipeline(question):

    documents = retrieve_documents(
        question
    )

    context = create_context(
        documents
    )

    answer = generate_answer(

        question,

        context

    )

    return answer, documents


# ==========================================================
# PART 13 - STREAMLIT UI
# ==========================================================

st.set_page_config(

    page_title="AI Document Q&A",

    page_icon="🤖",

    layout="wide"

)


# ==========================================================
# PART 14 - TITLE
# ==========================================================

st.title(
    "🤖 AI Document Q&A System"
)


st.write(
    "Ask questions about the knowledge base."
)


# ==========================================================
# PART 15 - USER INPUT
# ==========================================================

question = st.text_input(

    "Enter your question:"

)


# ==========================================================
# PART 16 - ASK BUTTON
# ==========================================================

if st.button(
    "Ask AI"
):

    if question.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching documents..."
        ):

            answer, documents = (
                rag_pipeline(question)
            )


        # ==================================================
        # DISPLAY ANSWER
        # ==================================================

        st.subheader(
            "Answer"
        )

        st.write(
            answer
        )


        # ==================================================
        # DISPLAY SOURCES
        # ==================================================

        st.subheader(
            "Retrieved Sources"
        )


        for i, document in enumerate(
            documents
        ):

            with st.expander(
                f"Source {i + 1}"
            ):

                st.write(
                    document.page_content
                )

                st.write(
                    "Metadata:",
                    document.metadata
                )


# ==========================================================
# END OF APPLICATION
# ==========================================================
