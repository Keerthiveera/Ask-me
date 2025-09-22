from flask import Flask, render_template, request, jsonify
import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Gemini API client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model = "gemini-2.5-flash"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    try:
        response = client.models.generate_content(
            model=model,
            contents=user_input
        )
        answer = response.text.strip()
    except Exception as e:
        answer = f"Error: {e}"
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
