# Week 6 — Word Embeddings & Mental Health Sentiment Analysis

## Overview

Two topics are covered this week:

1. **Word Embeddings** (`embeddings.ipynb`) — representing words as dense numerical vectors that capture semantic meaning, comparing Word2Vec, GloVe, and FastText.
2. **Mental Health Sentiment Analysis** (`mental_health.ipynb`) — a full ML pipeline that classifies mental health statements into diagnostic categories using classical NLP preprocessing and multiple classifiers.

---

## Word Embeddings (`embeddings.ipynb`)

### Word2Vec

A small Word2Vec model is trained from scratch using `gensim` on a toy corpus of three sentences. The model uses:
- `vector_size=50` — 50-dimensional embeddings
- `window=2` — context window of 2 words on each side
- `min_count=1` — include all words regardless of frequency

The following operations are demonstrated:
- Retrieving the embedding vector for a word (`model.wv["nlp"]`)
- Finding the most semantically similar words (`most_similar`)
- Computing the similarity score between two words (`similarity`)

### GloVe

Pre-trained GloVe vectors are loaded using `gensim.downloader` (`glove-wiki-gigaword-50`), which provides 50-dimensional vectors trained on Wikipedia and Gigaword corpora. The same operations are demonstrated:
- Vector lookup
- Most similar words
- Word similarity score

Using pre-trained vectors reflects how GloVe is typically used in practice, since it requires large corpora to produce meaningful embeddings.

### FastText

A FastText model is trained from scratch using `gensim.models.FastText` on the same toy corpus and with the same hyperparameters as the Word2Vec model (`vector_size=50`, `window=2`, `min_count=1`). The same three operations are demonstrated.

FastText differs from Word2Vec in that it represents each word as a sum of its character n-gram vectors, making it capable of producing embeddings for out-of-vocabulary words.

### Visualization

Word embeddings are visualized in 2D using PCA (`sklearn.decomposition.PCA`) to reduce the 50-dimensional vectors to two components, then plotted with `matplotlib`.

---

## Mental Health Sentiment Analysis (`mental_health.ipynb`)

A full end-to-end NLP classification pipeline built on `mental_health_data/Combined Data.csv`. Each row contains a free-text `statement` and a `status` label (e.g., Anxiety, Depression, Stress, Bipolar, Normal).

### 1. Data Cleaning

A custom `DataCheck` utility (from `functions.py`) is used to inspect the dataset:
- Identify and drop missing values (`dropna`)
- Identify and drop duplicate records (`drop_duplicates`)

### 2. Text Preprocessing Pipeline

Seven sequential steps applied to produce a `clean_text` column:

| Step | Operation |
|---|---|
| 1 | Lowercase all text |
| 2 | Remove punctuation (`string.punctuation`) |
| 3 | Tokenize (`nltk.word_tokenize`) |
| 4 | Remove stopwords (`nltk.corpus.stopwords`) |
| 5 | Lemmatize tokens (`WordNetLemmatizer`) |
| 6 | Re-join tokens back into a string |
| 7 | Label encode the `status` target column (`LabelEncoder`) |

### 3. Feature Extraction & Train/Test Split

- `TfidfVectorizer` converts cleaned text into TF-IDF feature matrices.
- 80/20 train-test split with `random_state=42`.

### 4. Modelling

A reusable `classifier()` function trains each model and prints training accuracy, training precision, testing accuracy, testing precision, and a confusion matrix (`ConfusionMatrixDisplay`). Five models were evaluated:

| Model | Notes |
|---|---|
| Multinomial Naive Bayes | Baseline probabilistic model |
| Logistic Regression | `max_iter=1000`; selected as final model |
| K-Nearest Neighbors | `n_neighbors=5` |
| Decision Tree | Default settings |
| Random Forest | `n_estimators=100` |

**Logistic Regression** was chosen as the final model based on performance.

### 5. Model Persistence

Both the trained model and vectorizer are serialized with `pickle` for reuse:
- `my_model.pkl` — the fitted Logistic Regression model
- `vectorizer.pkl` — the fitted TF-IDF vectorizer

### 6. Inference

A `predict_statement()` function applies the same preprocessing pipeline to new text, loads the saved model and vectorizer, and returns the decoded label. Example predictions tested:

- `"I feel anxious and stressed about my exams."` → Anxiety
- `"I have been feeling very down and hopeless lately."` → Depression
- Mixed emotional statement → tested for multi-label edge cases
- `"I feel amazing"` → Normal

---

## Technologies Used

| Category | Tools |
|---|---|
| Word Embeddings | gensim (Word2Vec, FastText), gensim.downloader (GloVe) |
| Visualization | matplotlib, sklearn PCA |
| Text Preprocessing | NLTK (tokenization, stopwords, lemmatization), string |
| Feature Extraction | sklearn TfidfVectorizer |
| Classifiers | sklearn (MultinomialNB, LogisticRegression, KNN, DecisionTree, RandomForest) |
| Evaluation | accuracy_score, precision_score, confusion_matrix, ConfusionMatrixDisplay |
| Model Persistence | pickle |