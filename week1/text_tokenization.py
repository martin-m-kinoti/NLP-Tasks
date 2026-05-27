# Libraries
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# User text
text = str(input("Enter text: "))

# Tokenize
tokens = word_tokenize(text)
print("Tokens: ")
print(tokens)
print("----------------------------")
print("Word count: ")
print(Counter(tokens))