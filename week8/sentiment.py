"""
Practical Task 1: Sentiment Analysis using HuggingFace Transformers
"""

from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

reviews = [
    {
        "label": "Positive Review",
        "text": "This product is absolutely amazing! The quality is outstanding and it exceeded all my expectations. I would highly recommend it to everyone."
    },
    {
        "label": "Negative Review",
        "text": "Terrible experience. The product broke after two days and customer support was completely unhelpful. Total waste of money."
    },
    {
        "label": "Neutral Statement",
        "text": "The package arrived on Tuesday. It contains three items as described on the website."
    }
]

print("-" * 60)
print("SENTIMENT ANALYSIS RESULTS")
print("-" * 60)

for review in reviews:
    result = sentiment_pipeline(review["text"])[0]
    print(f"\n[{review['label']}]")
    print(f"Text    : {review['text']}")
    print(f"Sentiment: {result['label']}")
    print(f"Confidence: {result['score']:.4f} ({result['score']*100:.2f}%)")

print("\n" + "-" * 60)
print("INTERPRETATION")
print("-" * 60)
print("""
- The positive review receives a POSITIVE label with high confidence
  because of strong positive words: 'amazing', 'outstanding', 'recommend'.
- The negative review receives a NEGATIVE label with high confidence
  due to words like 'terrible', 'broke', 'unhelpful', 'waste'.
- The neutral statement receives a label (often POSITIVE with lower
  confidence) because it is factual and lacks emotional language,
  showing the model defaults toward neutral/positive for bland text.
""")