import openai
import streamlit as st

# Set up the OpenAI API
openai.api_key = st.text_input("Enter your OpenAI API key:", type="password")
model_engine = "text-davinci-003"

# Define a function to extract information from a prompt using the OpenAI API
def extract_information(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=f"Extract the celebrity name, event and fashion items from this prompt: {prompt}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Set up the Streamlit app
st.title("OpenAI Text Extraction Demo")
prompt = st.text_input("Enter a prompt:")
if st.button("Extract information"):
    if not openai.api_key:
        st.error("Please enter your OpenAI API key")
    else:
        information = extract_information(prompt)
        st.write(information)
