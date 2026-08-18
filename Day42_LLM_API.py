# ==========================================================
# DAY 42 - LLM APIs + PRACTICAL LLM APPLICATION
# ==========================================================

# Install:
#
# pip install google-genai python-dotenv


# ==========================================================
# Q1. What is an LLM API?
# ==========================================================

# An LLM API allows our Python application to communicate
# with a hosted large language model.
#
# Basic flow:
#
# Python Application
#        ↓
#     API Request
#        ↓
#      LLM
#        ↓
#   API Response
#        ↓
# Python Application


# ==========================================================
# Q2. Import Required Libraries
# ==========================================================

import os

from dotenv import load_dotenv

from google import genai


# ==========================================================
# Q3. Load Environment Variables
# ==========================================================

load_dotenv()


# ==========================================================
# Q4. Get API Key
# ==========================================================

API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


if not API_KEY:

    raise ValueError(
        "GEMINI_API_KEY is not set."
    )


# ==========================================================
# Q5. Create LLM Client
# ==========================================================

client = genai.Client(
    api_key=API_KEY
)


# ==========================================================
# Q6. Send a Basic Prompt
# ==========================================================

response = client.models.generate_content(

    model="gemini-2.5-flash",

    contents="Explain machine learning in simple words."

)


print(
    "LLM Response:"
)

print(
    response.text
)


# ==========================================================
# Q7. Create a Reusable Function
# ==========================================================

def ask_llm(prompt):

    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=prompt

    )

    return response.text


answer = ask_llm(
    "What is SQL? Explain in 3 points."
)


print(
    answer
)


# ==========================================================
# Q8. Create a System Instruction
# ==========================================================

system_instruction = """
You are a technical interviewer.

Give concise and accurate answers
suitable for a fresher preparing
for data and AI interviews.
"""


# ==========================================================
# Q9. Use System Instruction
# ==========================================================

response = client.models.generate_content(

    model="gemini-2.5-flash",

    contents="Explain overfitting.",

    config={
        "system_instruction": system_instruction
    }

)


print(
    response.text
)


# ==========================================================
# Q10. System Instruction vs User Prompt
# ==========================================================

# System instruction:
# Defines the general behavior/role of the model.
#
# User prompt:
# Gives the specific task.
#
# Example:
#
# System:
# "You are a SQL interviewer."
#
# User:
# "Explain GROUP BY."


# ==========================================================
# Q11. Build a Resume Skill Extractor
# ==========================================================

resume_text = """
Python developer with experience in Python,
Pandas, NumPy, SQL, machine learning,
FastAPI and Docker.
"""


prompt = f"""
Extract the technical skills from the following
resume.

Return only a comma-separated list.

Resume:
{resume_text}
"""


skills = ask_llm(
    prompt
)


print(
    "Extracted Skills:"
)

print(
    skills
)


# ==========================================================
# Q12. Build an Interview Question Generator
# ==========================================================

topic = "Pandas"

prompt = f"""
Generate 5 important fresher interview questions
for {topic}.

For each question provide:
1. Question
2. Short answer
3. One practical example
"""


questions = ask_llm(
    prompt
)


print(
    questions
)


# ==========================================================
# Q13. Build a Text Summarizer
# ==========================================================

text = """
Machine learning is a branch of artificial intelligence
that enables computers to learn patterns from data.
Supervised learning uses labeled data, while
unsupervised learning finds patterns in unlabeled data.
"""


prompt = f"""
Summarize the following text in exactly 3 bullet points.

{text}
"""


summary = ask_llm(
    prompt
)


print(
    "Summary:"
)

print(
    summary
)


# ==========================================================
# Q14. Build a Sentiment Analyzer
# ==========================================================

review = """
The product is good and the delivery was very fast.
"""


prompt = f"""
Classify the sentiment of this review.

Return only:
Positive
Negative
Neutral

Review:
{review}
"""


sentiment = ask_llm(
    prompt
)


print(
    "Sentiment:"
)

print(
    sentiment
)


# ==========================================================
# Q15. Request Structured Output
# ==========================================================

prompt = """
Analyze this sentence:

"I love this laptop because it is fast."

Return JSON with:
sentiment
reason
"""


structured_response = client.models.generate_content(

    model="gemini-2.5-flash",

    contents=prompt,

    config={
        "response_mime_type": "application/json"
    }

)


print(
    "Structured Response:"
)

print(
    structured_response.text
)


# ==========================================================
# Q16. Add Error Handling
# ==========================================================

def safe_llm_call(prompt):

    try:

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        return response.text

    except Exception as e:

        return (
            f"LLM API Error: {e}"
        )


result = safe_llm_call(
    "Explain normalization in DBMS."
)


print(
    result
)


# ==========================================================
# Q17. Understand API Request and Response
# ==========================================================

print("""
APPLICATION

Prompt
   ↓
API Request
   ↓
LLM Provider
   ↓
Model Inference
   ↓
API Response
   ↓
Application
""")


# ==========================================================
# Q18. Why API Keys?
# ==========================================================

# API keys authenticate your application
# with the LLM provider.
#
# NEVER write:
#
# API_KEY = "my-secret-key"
#
# directly in code that will be uploaded to GitHub.


# ==========================================================
# Q19. Environment Variable
# ==========================================================

print("""
Environment Variable Example:

GEMINI_API_KEY=your_api_key_here

Python:

os.getenv("GEMINI_API_KEY")
""")


# ==========================================================
# Q20. Final LLM Application Architecture
# ==========================================================

print("""
USER
 ↓
PYTHON APPLICATION
 ↓
PROMPT
 ↓
LLM API
 ↓
LLM
 ↓
RESPONSE
 ↓
APPLICATION
 ↓
USER
""")


# ==========================================================
# END OF DAY 42
# ==========================================================
