# BIT4133-Week7-Neural-Language-Models

## Overview
Deep learning applied to NLP — text prediction, tokenization, and mental health sentiment classification.

## Files
| File | Description |
|---|---|
| `deep_learning.ipynb` | Three practical tasks: text prediction system, TensorFlow NLP exercise, and a mini predictive text GUI app |
| `mental_health.ipynb` | Mental health sentiment classification using TF-IDF + sklearn classifiers + a dense neural network |
| `Neural_Language_Models.docx` | 2-page research summary covering NLMs, RNNs, LSTMs, Transformers, and LLMs |

## Tasks Completed

### Text Prediction System
- Built a 20-sentence corpus and tokenized it with Keras `Tokenizer`
- Trained an `Embedding → LSTM(128) → Dense(softmax)` model for next-word prediction
- `predict_next_word()` returns top-N predictions with confidence scores

### TensorFlow NLP Exercise
- Tokenized sample texts, displayed full word-index mappings, and converted texts to padded integer sequences
- Reverse-decoded sequences back to words for verification

### Predictive Text App
- Extended corpus (50 sentences), deeper `LSTM(256) → LSTM(128)` model
- Tkinter GUI: input box, top-5 predictions with confidence bars, and status line
- Console demo with ASCII confidence bars for documentation screenshots

### Mental Health Sentiment Analysis (`mental_health.ipynb`)
- Cleaned and preprocessed 53k mental health statements (lowercase, punctuation removal, stopwords, lemmatization)
- Compared Naive Bayes, Logistic Regression, KNN, Decision Tree, and Random Forest classifiers
- Added a dense neural network (TF-IDF top-5000 features → `Dense(128/64/32) → softmax`) with training curves and confusion matrix