import openai
from flask import *
from dotenv import load_dotenv
import os
import streamlit as st

# initialize Flask app
# app = Flask(__name__)

load_dotenv()  # load environment variables from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/generate_translate", methods=["POST"])
def generate_translate(source_text, target_text):

    # source_text = request.form.get("source_text")
    # target_text = request.form.get("target_text")

    prompt = f"Translate from {source_text} to {target_text}:"

    Response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        # stop=["\n", " Translation:"],
    )
    # print("API response : ", Response["choices"][0]["text"].strip())

    translated_text = Response["choices"][0]["text"].strip()
    print("translated text : ", translated_text)

    return translated_text
    # return render_template("index.html", source_text = source_text, target_text = translated_text)

# Define the main function that sets up the Streamlit UI and handles the translation process
def main():
    # Set up the Streamlit UI
    st.sidebar.title('GPT Language Lion')
    st.sidebar.subheader('AI Powered Language Translation Tool')
    st.sidebar.caption('Enter text to translate and select the target language')
    
    # Create a text input for the user to enter the text to be translated
    text_input = st.text_area('Enter text to translate : ')
    
    # Create a selectbox for the user to select the target language
    target_language = st.text_input('Enter output language : ')

    # Create a button that the user can click to initiate the translation process
    translate_button = st.button('Translate')

    # Create a placeholder where the translated text will be displayed
    translated_text = st.empty()

    # Handle the translation process when the user clicks the translate button
    if translate_button:
        translated_text.text('Translating...')
        translated_text.text(generate_translate(text_input, target_language))

if __name__ == "__main__":
    main()
# if __name__ == "__main__":
#     app.run(debug=True)