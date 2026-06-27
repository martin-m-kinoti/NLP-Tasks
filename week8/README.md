# BIT4133 — Week 8: Transformer Models and Attention Mechanisms

## Overview
This week covered the theory and practical application of Transformer models and attention mechanisms in NLP.

## Files

| File | Description |
|------|-------------|
| `week8_activities.docx` | Class exercises and assignment report |
| `practical_task1_sentiment.py` | Sentiment analysis using HuggingFace Transformers |
| `practical_task2_text_generation.py` | Text generation using GPT-2 |

## Class Exercises

- Explained why Transformer models are suitable for a university student Q&A system, covering the role of attention mechanisms and three advantages over traditional RNN models (parallelisation, long-range dependencies, transfer learning).

- Analysed how self-attention resolves pronoun ambiguity in the sentence *"The doctor informed the patient that she would recover soon."*, identifying high-attention word pairs and discussing why context is critical in NLP.

## Tasks

**Task 1: Sentiment Analysis**
Uses the Transformer Model via HuggingFace pipeline to classify a positive review, negative review, and neutral statement. Results include confidence scores and interpretation.

**Task 2: Text Generation**
Loads GPT-2 to generate text continuations for predefined prompts, then enters an interactive loop for user-supplied prompts. Compares outputs across different prompt types (factual vs. narrative).

## Research
Research report on **BERT** covering:
- Architecture overview (decoder-only Transformer, token/positional embeddings, stacked layers)
- Working principle (language modelling objective, autoregressive generation, causal attention)
- Advantages, limitations, real-world applications
- Python implementation example using HuggingFace GPT-2

## Dependencies
```
transformers
torch
python-docx
```