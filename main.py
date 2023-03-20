import openai
from flask import *
from dotenv import load_dotenv
import os

# initialize Flask app
app = Flask(__name__)

load_dotenv()  # load environment variables from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_translate():
    source_text = request.form.get("source_text")
    target_text = request.form.get("target_text")

    Response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Translate from {target_text} to {source_text}:",
        temperature=0.9,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n", " Translation:"],
    )

    target_text = Response["choices"][0]["text"].strip()

    return render_template("index.html", source_text = source_text, target_text = target_text)

