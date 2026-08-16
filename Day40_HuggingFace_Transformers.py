# ==========================================================
# DAY 40 - HUGGING FACE TRANSFORMERS
# ==========================================================

from transformers import (
    pipeline,
    AutoTokenizer,
    AutoModelForSequenceClassification
)


# ==========================================================
# Q1. What is Hugging Face?
# ==========================================================

# Hugging Face provides tools and pretrained models
# for NLP, computer vision, audio and generative AI.
#
# Its Transformers library provides access to
# many pretrained Transformer models.


# ==========================================================
# Q2. Create a Sentiment Analysis Pipeline
# ==========================================================

sentiment_pipeline = pipeline(
    "sentiment-analysis"
)


# ==========================================================
# Q3. Perform Sentiment Analysis
# ==========================================================

text = "I really enjoyed this product."

result = sentiment_pipeline(
    text
)

print(
    "Sentiment:",
    result
)


# ==========================================================
# Q4. Test Positive and Negative Sentences
# ==========================================================

texts = [

    "The product is excellent.",

    "I really enjoyed the movie.",

    "The service was terrible.",

    "I hate this experience."

]


results = sentiment_pipeline(
    texts
)


for text, result in zip(
    texts,
    results
):

    print(
        text,
        "->",
        result
    )


# ==========================================================
# Q5. Understand Pipeline
# ==========================================================

# pipeline() simplifies the process:
#
# Text
#  ↓
# Tokenization
#  ↓
# Transformer Model
#  ↓
# Prediction
#
# Without pipeline(), we would manually perform
# tokenization and model inference.


# ==========================================================
# Q6. Create Text Classification Pipeline
# ==========================================================

classifier = pipeline(
    "text-classification"
)


classification = classifier(
    "Artificial intelligence is changing technology."
)


print(
    "Classification:",
    classification
)


# ==========================================================
# Q7. Load a Tokenizer
# ==========================================================

model_name = (
    "distilbert-base-uncased-finetuned-sst-2-english"
)


tokenizer = AutoTokenizer.from_pretrained(
    model_name
)


# ==========================================================
# Q8. Tokenize Text
# ==========================================================

text = "I love machine learning."

tokens = tokenizer(
    text
)


print(
    "Tokenized Input:"
)

print(tokens)


# ==========================================================
# Q9. Display Input IDs
# ==========================================================

print(
    "Input IDs:"
)

print(
    tokens["input_ids"]
)


# ==========================================================
# Q10. Convert Token IDs Back to Tokens
# ==========================================================

token_list = tokenizer.convert_ids_to_tokens(
    tokens["input_ids"]
)


print(
    "Tokens:"
)

print(
    token_list
)


# ==========================================================
# Q11. Load Pretrained Classification Model
# ==========================================================

model = AutoModelForSequenceClassification.from_pretrained(
    model_name
)


print(
    "Model Loaded Successfully"
)


# ==========================================================
# Q12. Understand Tokenizer + Model
# ==========================================================

print("""
TEXT
 ↓
TOKENIZER
 ↓
TOKEN IDs
 ↓
TRANSFORMER MODEL
 ↓
LOGITS
 ↓
PREDICTION
""")


# ==========================================================
# Q13. Tokenize Multiple Sentences
# ==========================================================

texts = [

    "Machine learning is interesting.",

    "I dislike this product."

]


batch = tokenizer(
    texts,
    padding=True,
    truncation=True,
    return_tensors="pt"
)


print(
    "Batch Input:"
)

print(
    batch
)


# ==========================================================
# Q14. Run Model Inference
# ==========================================================

outputs = model(
    **batch
)


print(
    "Model Outputs:"
)

print(
    outputs.logits
)


# ==========================================================
# Q15. Convert Logits to Predictions
# ==========================================================

predicted_class_ids = (
    outputs.logits.argmax(
        dim=-1
    )
)


print(
    "Predicted Class IDs:"
)

print(
    predicted_class_ids
)


# ==========================================================
# Q16. Get Model Labels
# ==========================================================

print(
    "Model Labels:"
)

print(
    model.config.id2label
)


# ==========================================================
# Q17. Text Generation Pipeline
# ==========================================================

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)


prompt = (
    "Artificial intelligence will"
)


generated_text = generator(
    prompt,
    max_new_tokens=30,
    num_return_sequences=1
)


print(
    "Generated Text:"
)

print(
    generated_text
)


# ==========================================================
# Q18. Understand Pretrained Models
# ==========================================================

print("""
PRETRAINED MODEL

Large Dataset
     ↓
Pretraining
     ↓
Transformer Model
     ↓
Reusable Model
     ↓
Fine-tuning / Inference
""")


# ==========================================================
# Q19. Model vs Tokenizer
# ==========================================================

print("""
TOKENIZER

Converts text into tokens/token IDs.

MODEL

Processes token representations and
produces predictions or representations.

Both are required to use most
Transformer models correctly.
""")


# ==========================================================
# Q20. Complete Hugging Face Workflow
# ==========================================================

print("""
HUGGING FACE WORKFLOW

Choose pretrained model
        ↓
Load tokenizer
        ↓
Input text
        ↓
Tokenization
        ↓
Token IDs
        ↓
Transformer model
        ↓
Inference
        ↓
Prediction / Generated text
""")


# ==========================================================
# END OF DAY 40
# ==========================================================
