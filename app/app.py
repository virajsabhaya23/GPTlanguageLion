import openai
from dotenv import load_dotenv
import os
import streamlit as st

# load environment variables from .env file
load_dotenv()

# Set up the Streamlit UI
st.sidebar.title('GPT Language Lion')
st.sidebar.subheader('AI Powered Language Translation Tool')
st.sidebar.caption('Enter text to translate and select the target language')

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = st.sidebar.text_input('Enter your OpenAI API Key', type='password')


def generate_translate(source_text, target_text):
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
    )
    # print("API response : ", Response["choices"][0]["text"].strip())
    translated_text = Response["choices"][0]["text"].strip()
    return translated_text


# Define the main function that sets up the Streamlit UI and handles the translation process
def main():
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