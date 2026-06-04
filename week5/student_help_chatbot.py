import os
from dotenv import load_dotenv
load_dotenv()   
from openai import OpenAI
from colorama import Fore, Style, init

init(autoreset=True)

client = OpenAI(api_key=os.getenv("API_KEY"))

SYSTEM_PROMPT = """
You are a helpful university student assistant.
You can only help with the following:

1. GREETINGS — Respond warmly to hello, hi, hey, good morning, etc.

2. CAT SCHEDULE — Answer questions about CATs (Continuous Assessment Tests):
   - CAT 1: Week 4 of the semester (Monday to Friday)
   - CAT 2: Week 8 of the semester (Monday to Friday)
   - CATs are held during normal lecture hours in the lecture halls
   - Students must carry their student ID to sit any CAT
   - Results are released within 2 weeks on the student portal

3. UNIT REGISTRATION — Answer questions about registering for units:
   - Registration opens at the start of each semester via the student portal
   - Students must register within the first 2 weeks or face a penalty
   - Maximum of 7 units per semester, minimum of 3
   - To register: log into portal → select semester → choose units → confirm
   - Late registration fee: KES 500

Rules:
- If the student asks about anything outside these 3 topics,
  reply: "I can only help with CAT schedules, and unit registration."
- Keep all responses short and clear (2-3 sentences max)
- Always be warm and encouraging
- If student says bye, goodbye, or exit — say farewell warmly
"""

history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def chat(user_input):
    history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=history,
        max_tokens=150,
        temperature=0.5,
    )

    reply = response.choices[0].message.content.strip()
    history.append({"role": "assistant", "content": reply})

    # trim history — keep system prompt + last 10 messages
    if len(history) > 11:
        history[1:3] = []

    return reply

def is_exit(text):
    return any(w in text.lower() for w in ["bye","goodbye","exit","quit","see you"])

def print_banner():
    print(Fore.CYAN  + "   University Student Assistant")
    print(Fore.CYAN  + "-" * 45)
    print(Fore.YELLOW + "   I can help with:")
    print(Fore.YELLOW + "   • CAT schedules")
    print(Fore.YELLOW + "   • Unit registration")
    print(Fore.CYAN  + "-" * 45)
    print(Fore.WHITE + "   Type 'bye' to exit\n")

def main():
    print_banner()
    while True:
        try:
            user = input(Fore.GREEN + "You: " + Style.RESET_ALL).strip()

            if not user:
                continue

            reply = chat(user)
            print(Fore.BLUE + "Raven: " + Style.RESET_ALL + reply + "\n")

            if is_exit(user):
                break

        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nRaven: Goodbye! Take care.")
            break

if __name__ == "__main__":
    main()