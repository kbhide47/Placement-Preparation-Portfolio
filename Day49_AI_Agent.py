# ==========================================================
# DAY 49 - AI AGENTS
# ==========================================================


# ==========================================================
# Q1. What is an AI Agent?
# ==========================================================

# An AI Agent is an AI system that can:
#
# 1. Understand a user's goal
# 2. Decide what action to take
# 3. Use tools
# 4. Observe tool results
# 5. Perform multiple steps
# 6. Produce a final answer
#
#
# Basic architecture:
#
# User
#   ↓
# Agent
#   ↓
# Decide Action
#   ↓
# Tool
#   ↓
# Tool Result
#   ↓
# Agent
#   ↓
# Final Answer


# ==========================================================
# Q2. LLM vs RAG vs AI Agent
# ==========================================================

print("""
LLM

User
 ↓
LLM
 ↓
Answer


RAG

User
 ↓
Retriever
 ↓
Documents
 ↓
LLM
 ↓
Answer


AI AGENT

User
 ↓
Agent
 ↓
Decide
 ↓
Tool
 ↓
Observe
 ↓
Decide
 ↓
Final Answer
""")


# ==========================================================
# Q3. What is a Tool?
# ==========================================================

# A tool is an external function or service
# that an AI agent can use.
#
# Examples:
#
# Calculator
# Search engine
# Database
# Python function
# Weather API
# Email API
# File reader
# SQL database
#
#
# Example:
#
# User:
# "Calculate 25 * 40"
#
# Agent:
# Uses calculator tool
#
# Calculator:
# 1000
#
# Agent:
# Returns 1000


# ==========================================================
# Q4. Create a Calculator Tool
# ==========================================================

def calculator(a, b, operation):

    if operation == "add":

        return a + b

    elif operation == "subtract":

        return a - b

    elif operation == "multiply":

        return a * b

    elif operation == "divide":

        if b == 0:

            return "Cannot divide by zero."

        return a / b

    else:

        return "Invalid operation."


print(
    calculator(
        20,
        5,
        "multiply"
    )
)


# ==========================================================
# Q5. Create a String Tool
# ==========================================================

def count_words(text):

    words = text.split()

    return len(words)


print(
    count_words(
        "Python is useful for AI"
    )
)


# ==========================================================
# Q6. Create a Simple Search Tool
# ==========================================================

knowledge = {

    "python":
        "Python is a programming language.",

    "pandas":
        "Pandas is used for data analysis.",

    "rag":
        "RAG combines retrieval with LLM generation.",

    "llm":
        "LLM stands for Large Language Model."

}


def search_knowledge(query):

    query = query.lower()

    for key, value in knowledge.items():

        if key in query:

            return value

    return "Information not found."


print(
    search_knowledge(
        "What is Pandas?"
    )
)


# ==========================================================
# Q7. What is Tool Calling?
# ==========================================================

# Tool calling means the LLM can decide that
# it needs an external tool and request that
# the application execute it.
#
#
# Example:
#
# User:
# "What is 25 * 50?"
#
# LLM:
# I need calculator.
#
# Application:
# Calls calculator(25, 50, multiply)
#
# Tool:
# 1250
#
# LLM:
# "The answer is 1250."


# ==========================================================
# Q8. Create Tool Registry
# ==========================================================

tools = {

    "calculator": calculator,

    "count_words": count_words,

    "search_knowledge": search_knowledge

}


print(
    tools
)


# ==========================================================
# Q9. Simple Agent Decision Function
# ==========================================================

def choose_tool(user_input):

    text = user_input.lower()

    if (
        "calculate" in text
        or "*" in text
        or "+" in text
        or "-" in text
    ):

        return "calculator"

    elif "word" in text:

        return "count_words"

    elif (
        "python" in text
        or "pandas" in text
        or "rag" in text
        or "llm" in text
    ):

        return "search_knowledge"

    else:

        return "unknown"


print(
    choose_tool(
        "Tell me about Pandas"
    )
)


# ==========================================================
# Q10. Create a Simple Agent
# ==========================================================

def simple_agent(user_input):

    tool = choose_tool(
        user_input
    )

    if tool == "search_knowledge":

        return search_knowledge(
            user_input
        )

    elif tool == "count_words":

        return count_words(
            user_input
        )

    elif tool == "calculator":

        return (
            "Calculator selected. "
            "Arguments need to be extracted."
        )

    else:

        return (
            "I don't know which tool to use."
        )


print(
    simple_agent(
        "What is RAG?"
    )
)


# ==========================================================
# Q11. What is Agent Workflow?
# ==========================================================

print("""
USER
 ↓
AGENT
 ↓
UNDERSTAND TASK
 ↓
SELECT TOOL
 ↓
EXECUTE TOOL
 ↓
OBSERVE RESULT
 ↓
DECIDE NEXT STEP
 ↓
FINAL ANSWER
""")


# ==========================================================
# Q12. What is ReAct?
# ==========================================================

# ReAct stands for:
#
# Reasoning + Acting
#
# Conceptually:
#
# Thought
#   ↓
# Action
#   ↓
# Observation
#   ↓
# Thought
#   ↓
# Action
#   ↓
# Observation
#   ↓
# Final Answer
#
# In real applications, the internal reasoning
# should not be exposed unnecessarily.


# ==========================================================
# Q13. Multi-Step Agent
# ==========================================================

def multi_step_agent():

    # Step 1
    data = search_knowledge(
        "What is Pandas?"
    )

    # Step 2
    word_count = count_words(
        data
    )

    # Step 3
    return {
        "information": data,
        "word_count": word_count
    }


result = multi_step_agent()


print(
    result
)


# ==========================================================
# Q14. What is Agent Memory?
# ==========================================================

# Memory allows an application to maintain
# relevant information across interactions.
#
# Example:
#
# User:
# "My name is Rahul."
#
# Later:
#
# User:
# "What is my name?"
#
# Agent:
# "Rahul."
#
# Modern applications may implement memory
# using conversation history, databases,
# summaries, or other storage.


# ==========================================================
# Q15. Simple Conversation Memory
# ==========================================================

conversation = []


def add_message(
    role,
    message
):

    conversation.append({

        "role": role,

        "message": message

    })


add_message(
    "user",
    "I am preparing for AI placements."
)

add_message(
    "assistant",
    "Focus on Python, ML, LLM and RAG."
)


print(
    conversation
)


# ==========================================================
# Q16. Agent + RAG
# ==========================================================

# An agent can use a RAG retriever as a tool.
#
#
# User:
# "Find the company's leave policy."
#
# Agent
#   ↓
# RAG Search Tool
#   ↓
# Relevant Documents
#   ↓
# Agent
#   ↓
# Answer
#
#
# This is more powerful than a simple RAG pipeline
# because the agent can decide WHEN to use retrieval.


# ==========================================================
# Q17. Agent + Multiple Tools
# ==========================================================

print("""
USER
 ↓
AI AGENT
 ├── Calculator
 ├── RAG Search
 ├── Database
 ├── Python
 └── Web Search
        ↓
   Final Answer
""")


# ==========================================================
# Q18. Why Use Agents?
# ==========================================================

# Agents are useful when a task requires
# multiple actions or tools.
#
# Example:
#
# "Analyze this sales dataset and tell me
# the most profitable category."
#
# Agent could:
#
# 1. Read the dataset
# 2. Analyze data
# 3. Calculate profit
# 4. Identify category
# 5. Explain result


# ==========================================================
# Q19. Agent vs Normal Python Program
# ==========================================================

print("""
NORMAL PROGRAM

Developer defines:
Step 1
Step 2
Step 3
Step 4


AI AGENT

Developer provides:
Tools + Instructions

Agent decides:
Which tool to use
and in what order.
""")


# ==========================================================
# Q20. Complete AI Agent Architecture
# ==========================================================

print("""
                   USER
                     ↓
                  AGENT
                     ↓
               UNDERSTAND GOAL
                     ↓
              DECIDE NEXT ACTION
                     ↓
              ┌──────┴──────┐
              ↓             ↓
          TOOL 1          TOOL 2
              ↓             ↓
          RESULT          RESULT
              └──────┬──────┘
                     ↓
                  AGENT
                     ↓
               FINAL ANSWER
""")


# ==========================================================
# END OF DAY 49
# ==========================================================
