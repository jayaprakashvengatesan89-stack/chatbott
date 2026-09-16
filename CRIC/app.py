from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

SYSTEM_PROMPT = """
You are CRIC, a cricket-specific AI chatbot.
Answer questions about cricket, player rankings, team rankings,
statistics, matches, tournaments, and cricket rules.
For unrelated questions, politely say you are a cricket-domain chatbot.
Do not invent current/live rankings. If current data is unavailable, say so.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"reply": "Please enter a cricket question."}), 400
    if not client:
        return jsonify({"reply": "Gemini API key is not configured. Add GEMINI_API_KEY to .env."}), 500
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=SYSTEM_PROMPT + "\n\nUser: " + message
        )
        return jsonify({"reply": response.text})
    except Exception:
        return jsonify({"reply": "Sorry, I could not process that request."}), 500

if __name__ == "__main__":
    app.run(debug=True)
