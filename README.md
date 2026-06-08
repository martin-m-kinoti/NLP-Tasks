# NLP Tasks

A summary of the Natural Language Processing concepts, techniques, and projects covered in this session.

---

## Overview

Topics progressed from classical techniques to modern transformer-based models and real-world deployment.

---

## 1. Introduction to NLP

**What was covered:**
Natural Language Processing as a field, and AI chatbots as one of its core application areas. The session explored how chatbots sit at the intersection of multiple NLP subfields.

**Key concepts:**
- NLU (Natural Language Understanding) — intent recognition, entity extraction, sentiment analysis
- Dialogue management — context tracking, slot filling, turn-taking
- NLG (Natural Language Generation) — producing fluent responses
- Types of chatbots: rule-based, retrieval-based, generative, task-oriented, open-domain

**Technologies introduced:**
spaCy, NLTK

---

## 2. Language Prediction

**What was covered:**
How NLP models predict the next most likely word or token given a context — the core mechanism behind text generation and chatbot responses.

**Key concepts:**
- N-gram language models and bigram probability estimation
- Probability distributions over vocabulary
- How LLMs (GPT, Claude) generate text one token at a time
- Applications: autocomplete, text generation, code completion, predictive typing

---

## 3. Sentence Analysis

**What was covered:**
Breaking down a sentence to understand its grammatical structure, meaning, and components. This is the foundational understanding layer of any NLP pipeline.

**Pipeline steps explored:**

| Step | Description |
|---|---|
| Tokenization | Splitting text into individual words or tokens |
| POS Tagging | Labeling each token with its grammatical role |
| Named Entity Recognition | Identifying people, places, organizations, dates |
| Parsing | Understanding how words relate to each other grammatically |
| Sentiment Analysis | Determining the emotional tone of a sentence |

---

## 4. Part-of-Speech Tagging & the Averaged Perceptron Tagger

**What was covered:**
The role of `nltk.download('averaged_perceptron_tagger')` and how POS tagging works as a classical NLP technique.

**Key concepts:**
- POS tags: NN (noun), VBZ (verb), JJ (adjective), DT (determiner), IN (preposition), NNP (proper noun)
- The averaged perceptron as a fast, accurate ML algorithm for sequence labeling
- How POS tagging feeds into entity extraction and intent detection in chatbots

---

## 5. Parsing

**What was covered:**
A deep dive into parsing — understanding how words in a sentence relate to and depend on each other.

**Two types explored:**

**Constituency parsing** — groups words into nested phrases (NP, VP) showing hierarchical structure.

**Dependency parsing** — shows word-to-word relationships, with every word pointing to the word it depends on.

**Key dependency labels:**
`ROOT` (main verb), `nsubj` (subject), `dobj` (direct object), `det` (determiner), `prep` (preposition), `pobj` (prepositional object)

**Tool used:** spaCy for dependency parsing

---

## 6. Hidden Markov Models & Sequence Labeling

**What was covered:**
HMMs as a statistical approach to sequence labeling — assigning tags to every token in a sequence.

**Core HMM components:**
- States
- Observations — visible words
- Transition probabilities
- Emission probabilities
- Initial probabilities

---


## 7. Classical vs AI Chatbots

**What was covered:**
A systematic comparison of rule-based (classical) chatbots versus AI-powered chatbots.

**Key differences:**
- Classical bots use keyword matching and decision trees; AI bots use ML and LLMs
- Classical bots fail on paraphrasing; AI bots understand meaning and intent
- Classical bots have no memory; AI bots maintain context across turns
- AI bots handle ambiguity, multiple languages, and unexpected inputs naturally

**AI chatbot pipeline:** Problem definition → Data collection → Preprocessing → NLU training → Dialogue management → Response generation → Knowledge base integration → Testing → Deployment → Monitoring

---

## 8. Building a Smart Student Help Chatbot

**What was covered:**
A complete, progressive build of a smart chatbot from scratch, moving through three implementations.

---

## Technologies Used 

| Category | Tools |
|---|---|
| Classical NLP | NLTK, spaCy, TextBlob |
| ML / Deep Learning | scikit-learn
| Datasets | Movie Reviews Dataset |
| API | OpenAI Python SDK |
| Environment | python-dotenv, os.getenv |

---
