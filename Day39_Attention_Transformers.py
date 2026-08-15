# ==========================================================
# DAY 39 - ATTENTION MECHANISM + TRANSFORMERS
# ==========================================================

import numpy as np


# ==========================================================
# Q1. What is Attention?
# ==========================================================

# Attention allows a model to determine which parts
# of the input are more important when processing
# a particular token.


# Example:
#
# "The cat sat on the mat because it was tired."
#
# "it" should pay attention to "cat"
# to understand what "it" refers to.


# ==========================================================
# Q2. Create Query, Key and Value Matrices
# ==========================================================

Q = np.array([
    [1, 0, 1],
    [0, 1, 1]
])


K = np.array([
    [1, 0, 1],
    [0, 1, 1]
])


V = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


print("Query:")
print(Q)

print("Key:")
print(K)

print("Value:")
print(V)


# ==========================================================
# Q3. Calculate Q × K Transpose
# ==========================================================

scores = np.matmul(
    Q,
    K.T
)


print(
    "Attention Scores:"
)

print(scores)


# ==========================================================
# Q4. Scale the Attention Scores
# ==========================================================

d_k = K.shape[1]

scaled_scores = (
    scores /
    np.sqrt(d_k)
)


print(
    "Scaled Scores:"
)

print(
    scaled_scores
)


# ==========================================================
# Q5. Create Softmax Function
# ==========================================================

def softmax(x):

    exp_x = np.exp(
        x - np.max(
            x,
            axis=-1,
            keepdims=True
        )
    )

    return (
        exp_x /
        np.sum(
            exp_x,
            axis=-1,
            keepdims=True
        )
    )


# ==========================================================
# Q6. Calculate Attention Weights
# ==========================================================

attention_weights = softmax(
    scaled_scores
)


print(
    "Attention Weights:"
)

print(
    attention_weights
)


# ==========================================================
# Q7. Calculate Attention Output
# ==========================================================

attention_output = np.matmul(
    attention_weights,
    V
)


print(
    "Attention Output:"
)

print(
    attention_output
)


# ==========================================================
# Q8. Complete Scaled Dot-Product Attention
# ==========================================================

def scaled_dot_product_attention(
    Q,
    K,
    V
):

    d_k = K.shape[-1]

    scores = np.matmul(
        Q,
        K.T
    )

    scaled_scores = (
        scores /
        np.sqrt(d_k)
    )

    weights = softmax(
        scaled_scores
    )

    output = np.matmul(
        weights,
        V
    )

    return output, weights


output, weights = (
    scaled_dot_product_attention(
        Q,
        K,
        V
    )
)


print(
    "Final Attention Output:"
)

print(output)


print(
    "Final Attention Weights:"
)

print(weights)


# ==========================================================
# Q9. Why Divide by sqrt(d_k)?
# ==========================================================

# When the dimensions of the vectors become large,
# dot-product values can become very large.
#
# Large values can make Softmax extremely concentrated.
#
# Scaling by sqrt(d_k) helps stabilize the values.


# ==========================================================
# Q10. Self-Attention
# ==========================================================

# In self-attention:
#
# Q, K and V are generated from the SAME input sequence.
#
# This allows every token to interact with other tokens
# in the same sequence.


sentence = [
    "The",
    "cat",
    "is",
    "sleeping"
]


print(
    "Sentence:"
)

print(sentence)


# ==========================================================
# Q11. Understand Query, Key and Value
# ==========================================================

print("""
QUERY:
What information am I looking for?

KEY:
What information do I contain?

VALUE:
What information should I pass forward?
""")


# ==========================================================
# Q12. Multi-Head Attention
# ==========================================================

# Instead of performing attention only once,
# Transformers use multiple attention heads.
#
# Different heads can learn different relationships.
#
# Example:
#
# Head 1 -> grammatical relationships
# Head 2 -> positional relationships
# Head 3 -> semantic relationships
#
# The outputs are combined.


# ==========================================================
# Q13. Positional Encoding
# ==========================================================

# Attention itself does not inherently understand
# the order of tokens.
#
# Positional information is therefore added to
# token representations.


# Example:
#
# "Dog bites man"
#
# is different from
#
# "Man bites dog"


# ==========================================================
# Q14. Transformer Encoder
# ==========================================================

print("""
TRANSFORMER ENCODER

Input Tokens
     ↓
Token Embeddings
     ↓
Positional Information
     ↓
Multi-Head Self-Attention
     ↓
Feed Forward Neural Network
     ↓
Normalization
     ↓
Output Representation
""")


# ==========================================================
# Q15. Transformer Decoder
# ==========================================================

print("""
TRANSFORMER DECODER

Previous Output Tokens
        ↓
Token Embeddings
        ↓
Positional Information
        ↓
Masked Self-Attention
        ↓
Cross Attention
        ↓
Feed Forward Network
        ↓
Next Token Prediction
""")


# ==========================================================
# Q16. Encoder vs Decoder
# ==========================================================

print("""
ENCODER

Main purpose:
Understand input.

Examples:
BERT


DECODER

Main purpose:
Generate output.

Examples:
GPT


ENCODER-DECODER

Main purpose:
Transform one sequence into another.

Example:
T5
""")


# ==========================================================
# Q17. Why Transformers?
# ==========================================================

print("""
TRANSFORMERS

Advantages:

1. Parallel processing
2. Captures long-range relationships
3. Better scalability
4. Works well with large datasets
5. Foundation of modern LLMs
""")


# ==========================================================
# Q18. RNN vs Transformer
# ==========================================================

print("""
RNN

Processes tokens sequentially.

Token 1
  ↓
Token 2
  ↓
Token 3
  ↓
Token 4


TRANSFORMER

Uses attention to process relationships
between tokens more directly.

Token 1 ←→ Token 2
   ↕          ↕
Token 3 ←→ Token 4
""")


# ==========================================================
# Q19. Transformer → LLM Connection
# ==========================================================

print("""
TRANSFORMER
     ↓
Large-scale Transformer
     ↓
Pretraining on huge text datasets
     ↓
Large Language Model
     ↓
GPT / Llama / etc.
     ↓
Text Generation
""")


# ==========================================================
# Q20. Final Transformer Workflow
# ==========================================================

print("""
TRANSFORMER WORKFLOW

Text
 ↓
Tokenization
 ↓
Token IDs
 ↓
Embeddings
 ↓
Positional Information
 ↓
Self-Attention
 ↓
Multi-Head Attention
 ↓
Feed Forward Network
 ↓
Multiple Transformer Layers
 ↓
Output
 ↓
Next Token Prediction
""")


# ==========================================================
# END OF DAY 39
# ==========================================================
