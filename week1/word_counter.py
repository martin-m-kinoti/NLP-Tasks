from collections import Counter

# User text
text = str(input("Enter text: "))

# Tokens
tokens = text.lower().split()

# Word count
print("Word Count: \n", Counter(tokens))