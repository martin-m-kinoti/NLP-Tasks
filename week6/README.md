# Week 6 — Word Embeddings

## Overview

This week explores word embedding techniques — methods for representing words as dense numerical vectors that capture semantic meaning. Three embedding approaches are implemented and compared in `embeddings.ipynb`.

---

## Word2Vec

A small Word2Vec model is trained from scratch using `gensim` on a toy corpus of three sentences. The model uses:
- `vector_size=50` — 50-dimensional embeddings
- `window=2` — context window of 2 words on each side
- `min_count=1` — include all words regardless of frequency

The following operations are demonstrated:
- Retrieving the embedding vector for a word (`model.wv["nlp"]`)
- Finding the most semantically similar words (`most_similar`)
- Computing the similarity score between two words (`similarity`)

---

## GloVe

Pre-trained GloVe vectors are loaded using `gensim.downloader` (`glove-wiki-gigaword-50`), which provides 50-dimensional vectors trained on Wikipedia and Gigaword corpora. The same operations are demonstrated:
- Vector lookup
- Most similar words
- Word similarity score

Using pre-trained vectors here reflects how GloVe is typically used in practice, since it requires large corpora to produce meaningful embeddings.

---

## FastText

A FastText model is trained from scratch using `gensim.models.FastText` on the same toy corpus and with the same hyperparameters as the Word2Vec model (`vector_size=50`, `window=2`, `min_count=1`). The same three operations are demonstrated.

FastText differs from Word2Vec in that it represents each word as a sum of its character n-gram vectors, making it capable of producing embeddings for out-of-vocabulary words.