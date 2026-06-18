from django.shortcuts import render

# Create your views here.
import json
import os
from dotenv            import load_dotenv
load_dotenv()
from django.http       import JsonResponse
from django.views      import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from openai            import OpenAI
from .prompt           import SYSTEM_PROMPT

client = OpenAI(api_key=os.getenv("API_KEY"))

# In-memory session store (keyed by session_id)
# For production replace with a database or Redis
sessions = {}

def get_history(session_id):
    if session_id not in sessions:
        sessions[session_id] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
    return sessions[session_id]

def trim_history(history, max_messages=10):
    # Always keep system prompt + last max_messages
    if len(history) > max_messages + 1:
        history[1:3] = []
    return history

def is_exit(text):
    return any(
        w in text.lower()
        for w in ["bye", "goodbye", "exit", "quit", "see you"]
    )

@method_decorator(csrf_exempt, name="dispatch")
class ChatView(View):

    def get(self, request):
        return JsonResponse({
            "message": "Student Chatbot API is running.",
            "usage":   "POST /api/chat/ with JSON body: {session_id, message}"
        })

    def post(self, request):
        try:
            body       = json.loads(request.body)
            user_input = body.get("message", "").strip()
            session_id = body.get("session_id", "default")
        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON body."},
                status=400
            )

        if not user_input:
            return JsonResponse(
                {"error": "Message cannot be empty."},
                status=400
            )

        history = get_history(session_id)
        history.append({"role": "user", "content": user_input})
        history = trim_history(history)

        try:
            response = client.chat.completions.create(
                model       = "gpt-3.5-turbo",
                messages    = history,
                max_tokens  = 150,
                temperature = 0.5,
            )
            reply = response.choices[0].message.content.strip()

        except Exception as e:
            return JsonResponse(
                {"error": f"OpenAI error: {str(e)}"},
                status=502
            )

        history.append({"role": "assistant", "content": reply})
        sessions[session_id] = history

        exiting = is_exit(user_input)
        if exiting:
            sessions.pop(session_id, None)     # clear session on exit

        return JsonResponse({
            "session_id": session_id,
            "message":    user_input,
            "reply":      reply,
            "exiting":    exiting,
        })