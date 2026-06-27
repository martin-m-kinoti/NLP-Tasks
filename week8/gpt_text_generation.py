"""
Practical Task 2: Text Generation using GPT-2
"""

from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate_text(prompt: str, max_length: int = 100, num_sequences: int = 1) -> list[dict]:
    results = generator(
        prompt,
        max_length=max_length,
        num_return_sequences=num_sequences,
        truncation=True,
        pad_token_id=50256
    )
    return results


def display_results(prompt: str, results: list[dict]) -> None:
    print(f"\nPrompt: \"{prompt}\"")
    print("-" * 60)
    for i, result in enumerate(results, 1):
        generated = result["generated_text"][len(prompt):]
        print(f"Continuation {i}:\n{generated.strip()}\n")


prompts = [
    "Artificial intelligence is transforming education by",
    "Once upon a time in a distant galaxy,",
    "The most important skill for a software engineer is",
    "Climate change poses a serious threat because"
]

print("-" * 60)
print("GPT-2 TEXT GENERATION")
print("-" * 60)

for prompt in prompts:
    results = generate_text(prompt, max_length=80)
    display_results(prompt, results)

print("-" * 60)
print("COMPARISON NOTES")
print("-" * 60)
print("""
- Factual prompts (AI, engineering) tend to yield coherent continuations
  that stay on topic, reflecting training data patterns.
- Narrative/creative prompts ('Once upon a time') produce more varied
  and imaginative text because story structures are common in training.
- GPT-2 does not guarantee factual accuracy; outputs reflect statistical
  patterns, not verified knowledge.
- Shorter max_length constrains creativity; increasing it allows richer
  but potentially less coherent continuations.
""")

print("\n--- Interactive Mode ---")
print("Type a sentence to generate a continuation (or 'quit' to exit).")
while True:
    user_input = input("\nEnter prompt: ").strip()
    if user_input.lower() in ("quit", "exit", "q"):
        break
    if not user_input:
        continue
    results = generate_text(user_input, max_length=100)
    display_results(user_input, results)
