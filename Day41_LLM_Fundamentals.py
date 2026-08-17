# ==========================================================
# DAY 41 - LLM FUNDAMENTALS
# ==========================================================

from transformers import AutoTokenizer


# ==========================================================
# Q1. What is an LLM?
# ==========================================================

# LLM = Large Language Model.
#
# It is a neural network trained on a very large amount
# of text to understand and generate language.
#
# Examples:
#
# GPT
# Llama
# Claude
# Gemini
# Mistral


# ==========================================================
# Q2. What is a Token?
# ==========================================================

# LLMs do not directly process normal human sentences.
# Text is first converted into tokens.
#
# A token can be:
#
# - a complete word
# - part of a word
# - punctuation
#
# Example:
#
# "I love Python"
#
# may become something like:
#
# ["I", "love", "Python"]


# ==========================================================
# Q3. Load a Tokenizer
# ==========================================================

model_name = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(
    model_name
)


# ==========================================================
# Q4. Tokenize Text
# ==========================================================

text = "I am learning artificial intelligence."

tokens = tokenizer.tokenize(
    text
)

print(
    "Tokens:"
)

print(tokens)


# ==========================================================
# Q5. Convert Tokens to IDs
# ==========================================================

token_ids = tokenizer.convert_tokens_to_ids(
    tokens
)

print(
    "Token IDs:"
)

print(token_ids)


# ==========================================================
# Q6. Convert Text Directly into Token IDs
# ==========================================================

encoded = tokenizer(
    text
)

print(
    "Encoded Text:"
)

print(encoded)


# ==========================================================
# Q7. Decode Token IDs
# ==========================================================

decoded_text = tokenizer.decode(
    encoded["input_ids"]
)

print(
    "Decoded Text:"
)

print(decoded_text)


# ==========================================================
# Q8. What is an LLM Token Limit?
# ==========================================================

# An LLM can process only a limited amount of tokens
# in one context.
#
# This limit is called the context window.
#
# Example:
#
# User Input
# +
# Previous Conversation
# +
# Retrieved Documents
# +
# System Instructions
#
# must fit within the model's context window.


# ==========================================================
# Q9. Understand Context Window
# ==========================================================

conversation = [

    "User: Explain machine learning.",

    "Assistant: Machine learning allows computers",
    "to learn patterns from data.",

    "User: Give me an example."

]


print(
    "Conversation:"
)

print(
    conversation
)


# ==========================================================
# Q10. What is Next Token Prediction?
# ==========================================================

# Many generative LLMs generate text by predicting
# the next token based on previous tokens.
#
# Example:
#
# "Python is a"
#
# Possible next token:
#
# "programming"
#
# Then:
#
# "Python is a programming"
#
# Possible next token:
#
# "language"


# ==========================================================
# Q11. Understand LLM Generation
# ==========================================================

print("""
PROMPT
  ↓
TOKENIZATION
  ↓
TOKEN IDs
  ↓
EMBEDDINGS
  ↓
TRANSFORMER
  ↓
PROBABILITY DISTRIBUTION
  ↓
NEXT TOKEN
  ↓
REPEAT
  ↓
FINAL RESPONSE
""")


# ==========================================================
# Q12. What is Temperature?
# ==========================================================

# Temperature controls randomness during generation.
#
# Lower temperature:
# More predictable / focused output.
#
# Higher temperature:
# More diverse / creative output.
#
# Typical conceptual example:
#
# temperature = 0.1
# → more deterministic
#
# temperature = 1.0
# → more diverse


temperature = 0.2

print(
    "Temperature:",
    temperature
)


# ==========================================================
# Q13. What is Top-K?
# ==========================================================

# Top-K limits token selection to the K most probable
# candidate tokens.
#
# Example:
#
# top_k = 5
#
# The model considers only the 5 highest-probability
# candidate tokens.


top_k = 5

print(
    "Top K:",
    top_k
)


# ==========================================================
# Q14. What is Top-P?
# ==========================================================

# Top-P (nucleus sampling) selects from the smallest
# group of tokens whose cumulative probability reaches P.
#
# Example:
#
# top_p = 0.9
#
# Select from tokens covering approximately 90%
# of cumulative probability.


top_p = 0.9

print(
    "Top P:",
    top_p
)


# ==========================================================
# Q15. Pretraining
# ==========================================================

print("""
PRETRAINING

Huge Dataset
     ↓
Tokenization
     ↓
Transformer
     ↓
Learn Language Patterns
     ↓
Pretrained Model
""")


# ==========================================================
# Q16. Fine-Tuning
# ==========================================================

print("""
FINE-TUNING

Pretrained Model
       ↓
Task-Specific Dataset
       ↓
Additional Training
       ↓
Specialized Model
""")


# ==========================================================
# Q17. Pretraining vs Fine-Tuning
# ==========================================================

print("""
PRETRAINING

Purpose:
Learn general language patterns.

Dataset:
Very large and diverse.

Result:
General-purpose model.


FINE-TUNING

Purpose:
Adapt model to a specific task/domain.

Dataset:
Smaller task-specific dataset.

Result:
Specialized model.
""")


# ==========================================================
# Q18. What is Inference?
# ==========================================================

# Inference means using a trained model to produce
# an output for new input.
#
# Training:
#
# Data → Model learns
#
# Inference:
#
# Input → Trained Model → Output


print(
    "Inference means using a trained model to make predictions."
)


# ==========================================================
# Q19. What is Hallucination?
# ==========================================================

# Hallucination occurs when an LLM produces information
# that sounds plausible but is incorrect, unsupported,
# or fabricated.


print(
    "LLM hallucination = confident but unsupported or incorrect output."
)


# ==========================================================
# Q20. LLM vs Traditional Machine Learning
# ==========================================================

print("""
TRADITIONAL ML

Dataset
   ↓
Feature Engineering
   ↓
ML Algorithm
   ↓
Prediction


LLM

Large Text Dataset
       ↓
Tokenization
       ↓
Transformer
       ↓
Pretraining
       ↓
LLM
       ↓
Prompt
       ↓
Generated Output
""")


# ==========================================================
# Q21. What is Prompt?
# ==========================================================

prompt = """
Explain machine learning in simple words
for a college student.
"""

print(
    "Prompt:"
)

print(prompt)


# ==========================================================
# Q22. What is Prompt Engineering?
# ==========================================================

# Prompt engineering means designing instructions/input
# that guide an LLM toward a useful and reliable output.


# ==========================================================
# Q23. Zero-Shot Prompting
# ==========================================================

zero_shot_prompt = """
Classify this sentence as positive or negative:

"I love this product."
"""

print(
    zero_shot_prompt
)


# ==========================================================
# Q24. Few-Shot Prompting
# ==========================================================

few_shot_prompt = """
Positive:
"I love this phone."

Negative:
"I hate this phone."

Classify:
"The phone is excellent."
"""

print(
    few_shot_prompt
)


# ==========================================================
# Q25. Complete LLM Workflow
# ==========================================================

print("""
USER PROMPT
     ↓
TOKENIZATION
     ↓
TOKEN IDs
     ↓
EMBEDDINGS
     ↓
TRANSFORMER LAYERS
     ↓
NEXT-TOKEN PROBABILITIES
     ↓
SAMPLING / DECODING
     ↓
NEXT TOKEN
     ↓
REPEAT
     ↓
FINAL RESPONSE
""")


# ==========================================================
# END OF DAY 41
# ==========================================================
