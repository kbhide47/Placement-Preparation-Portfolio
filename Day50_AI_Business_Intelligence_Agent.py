# ==========================================================
# DAY 50 - FINAL AI BUSINESS INTELLIGENCE AGENT
# ==========================================================


# ==========================================================
# Q1. What are we building?
# ==========================================================

# We are building an AI Business Intelligence Assistant.
#
# It can:
#
# 1. Analyze sales data
# 2. Calculate business metrics
# 3. Search business knowledge
# 4. Answer questions using an LLM
# 5. Use different tools depending on the question
#
#
# Example:
#
# User:
# "What is the total sales?"
#
# Agent
#   ↓
# Data Analysis Tool
#   ↓
# Pandas
#   ↓
# Result
#   ↓
# LLM
#   ↓
# Answer


# ==========================================================
# Q2. Import Libraries
# ==========================================================

import os

import pandas as pd

from dotenv import load_dotenv

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from langchain_core.documents import (
    Document
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)


# ==========================================================
# Q3. Load Environment Variables
# ==========================================================

load_dotenv()

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

if not API_KEY:

    raise ValueError(
        "GEMINI_API_KEY is not configured."
    )


# ==========================================================
# Q4. Load LLM
# ==========================================================

llm = ChatGoogleGenerativeAI(

    model="gemini-2.5-flash",

    google_api_key=API_KEY,

    temperature=0.2

)


# ==========================================================
# Q5. Load Sales Dataset
# ==========================================================

df = pd.read_csv(
    "data/sales.csv"
)


print(
    "Dataset shape:",
    df.shape
)


# ==========================================================
# Q6. Basic Data Cleaning
# ==========================================================

df = df.drop_duplicates()

df = df.dropna()


print(
    "Cleaned dataset shape:",
    df.shape
)


# ==========================================================
# Q7. Total Sales Tool
# ==========================================================

def total_sales():

    return df["Sales"].sum()


# ==========================================================
# Q8. Total Profit Tool
# ==========================================================

def total_profit():

    return df["Profit"].sum()


# ==========================================================
# Q9. Average Sales Tool
# ==========================================================

def average_sales():

    return df["Sales"].mean()


# ==========================================================
# Q10. Best Category Tool
# ==========================================================

def best_category():

    category_sales = (

        df.groupby("Category")["Sales"]

        .sum()

        .sort_values(
            ascending=False
        )

    )

    return category_sales


# ==========================================================
# Q11. Best Subcategory Tool
# ==========================================================

def best_subcategory():

    subcategory_sales = (

        df.groupby("Sub-Category")["Sales"]

        .sum()

        .sort_values(
            ascending=False
        )

    )

    return subcategory_sales


# ==========================================================
# Q12. Profit by Category
# ==========================================================

def profit_by_category():

    result = (

        df.groupby("Category")["Profit"]

        .sum()

        .sort_values(
            ascending=False
        )

    )

    return result


# ==========================================================
# Q13. Dataset Summary Tool
# ==========================================================

def dataset_summary():

    return {

        "rows": df.shape[0],

        "columns": df.shape[1],

        "total_sales":
            float(
                df["Sales"].sum()
            ),

        "total_profit":
            float(
                df["Profit"].sum()
            ),

        "average_sales":
            float(
                df["Sales"].mean()
            )

    }


# ==========================================================
# Q14. Create Business Knowledge Base
# ==========================================================

business_documents = [

    Document(

        page_content="""
        Sales performance should be evaluated using
        revenue, profit, quantity, discounts and
        customer segments.

        High sales do not always mean high profit.
        Excessive discounts can reduce profitability.
        """,

        metadata={
            "source":
            "business_knowledge.txt"
        }

    ),

    Document(

        page_content="""
        Business analysis can identify high-performing
        categories, low-profit products, customer
        segments and regional performance.

        Managers can use these insights to improve
        pricing, inventory and marketing decisions.
        """,

        metadata={
            "source":
            "business_knowledge.txt"
        }

    )

]


# ==========================================================
# Q15. Create Text Chunks
# ==========================================================

splitter = RecursiveCharacterTextSplitter(

    chunk_size=300,

    chunk_overlap=50

)


chunks = splitter.split_documents(

    business_documents

)


# ==========================================================
# Q16. Create Embeddings
# ==========================================================

embeddings = HuggingFaceEmbeddings(

    model_name=
    "sentence-transformers/all-MiniLM-L6-v2"

)


# ==========================================================
# Q17. Create FAISS Vector Store
# ==========================================================

vector_store = FAISS.from_documents(

    chunks,

    embeddings

)


# ==========================================================
# Q18. Create RAG Search Tool
# ==========================================================

def search_business_knowledge(
    query
):

    results = (

        vector_store.similarity_search(

            query,

            k=2

        )

    )

    context = "\n\n".join(

        document.page_content

        for document in results

    )

    return context


# ==========================================================
# Q19. Create Tool Selection Logic
# ==========================================================

def choose_tool(
    question
):

    question = question.lower()


    if (
        "total sales" in question
        or "revenue" in question
    ):

        return "total_sales"


    elif (
        "total profit" in question
        or "profit" in question
    ):

        return "total_profit"


    elif (
        "average sales" in question
        or "average revenue" in question
    ):

        return "average_sales"


    elif (
        "best category" in question
        or "top category" in question
    ):

        return "best_category"


    elif (
        "subcategory" in question
        or "sub-category" in question
    ):

        return "best_subcategory"


    elif (
        "business"
        in question
        or "strategy"
        in question
        or "discount"
        in question
    ):

        return "rag"


    else:

        return "general"


# ==========================================================
# Q20. Execute Tool
# ==========================================================

def execute_tool(
    tool,
    question
):


    if tool == "total_sales":

        return str(
            total_sales()
        )


    elif tool == "total_profit":

        return str(
            total_profit()
        )


    elif tool == "average_sales":

        return str(
            average_sales()
        )


    elif tool == "best_category":

        return str(
            best_category()
        )


    elif tool == "best_subcategory":

        return str(
            best_subcategory()
        )


    elif tool == "rag":

        return search_business_knowledge(
            question
        )


    else:

        return ""


# ==========================================================
# Q21. Generate Final Answer
# ==========================================================

def generate_answer(
    question,
    tool,
    result
):


    prompt = f"""
You are an AI Business Intelligence Assistant.

Answer the user's question using the
provided tool result.

Question:
{question}

Selected Tool:
{tool}

Tool Result:
{result}

Rules:

1. Do not invent numerical values.
2. Use the tool result when answering.
3. Explain the result clearly.
4. Keep the answer concise.
5. If information is unavailable,
   clearly say so.

Answer:
"""


    response = llm.invoke(
        prompt
    )

    return response.content


# ==========================================================
# Q22. Complete AI Agent
# ==========================================================

def business_agent(
    question
):

    # Step 1:
    # Decide which tool is required.

    tool = choose_tool(
        question
    )


    # Step 2:
    # Execute selected tool.

    result = execute_tool(

        tool,

        question

    )


    # Step 3:
    # Generate final answer.

    answer = generate_answer(

        question,

        tool,

        result

    )


    return {

        "tool": tool,

        "result": result,

        "answer": answer

    }


# ==========================================================
# Q23. Test Agent
# ==========================================================

questions = [

    "What is the total sales?",

    "What is the total profit?",

    "What is the average sales?",

    "Which is the best category?",

    "Which subcategory has the highest sales?",

    "How can discounts affect profit?",

    "Give me a business recommendation."

]


for question in questions:

    print(
        "\nQUESTION:"
    )

    print(
        question
    )


    result = business_agent(
        question
    )


    print(
        "\nSELECTED TOOL:"
    )

    print(
        result["tool"]
    )


    print(
        "\nANSWER:"
    )

    print(
        result["answer"]
    )


# ==========================================================
# Q24. Complete Architecture
# ==========================================================

print("""
                 USER
                   ↓
            STREAMLIT APP
                   ↓
             AI AGENT
                   ↓
          UNDERSTAND QUESTION
                   ↓
             TOOL SELECTION
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     PANDAS       RAG     CALCULATOR
        ↓          ↓          ↓
     DATA       FAISS      PYTHON
    ANALYSIS      ↓
        ↓       CONTEXT
        └──────────┼──────────┘
                   ↓
                  LLM
                   ↓
             FINAL ANSWER
""")


# ==========================================================
# Q25. Resume Description
# ==========================================================

resume_description = """
Built an AI Business Intelligence Assistant
using Python, Pandas, LangChain, FAISS and
Gemini LLM. Implemented data analysis tools,
semantic retrieval and RAG-based business
knowledge search, enabling the agent to select
appropriate tools and generate grounded
business insights.
"""


print(
    resume_description
)


# ==========================================================
# END OF DAY 50
# ==========================================================
