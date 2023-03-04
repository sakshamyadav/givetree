import streamlit as st
import openai

def generate_text(prompt, api_key):
    openai.api_key = api_key
    model_engine = "text-davinci-002"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=2048)
    message = completions.choices[0].text
    return message.strip()

st.title("Celebrity Outfit Finder")

api_key = st.text_input("Enter your OpenAI API key:")
celebrity_name = st.text_input("Enter the celebrity name:")
event_name = st.text_input("Enter the event name:")

if st.button("Find Outfit"):
    prompt = f"What did {celebrity_name} wear to {event_name}?"
    result = generate_text(prompt, api_key)
    prompt = f"extract key information from: {result}"
    entities = generate_text(prompt, api_key)
    st.write(result)
