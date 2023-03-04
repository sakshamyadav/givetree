import streamlit as st
import openai

def generate_text(prompt, api_key):
    openai.api_key = api_key
    model_engine = "text-davinci-002"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024)
    message = completions.choices[0].text
    return message.strip()

def extract_keywords(text):
    openai.api_key = api_key
    model_engine = "text-davinci-002"
    completions = openai.Completion.create(engine=model_engine, prompt=text, max_tokens=1024,
                                            model="text-davinci-002", 
                                            model_output_prefix="ENTITIES:\n")
    entities_text = completions.choices[0].text
    entities = entities_text.split("\n")[1:-1]
    return entities

st.title("Celebrity Outfit Finder")

api_key = st.text_input("Enter your OpenAI API key:")
celebrity_name = st.text_input("Enter the celebrity name:")
event_name = st.text_input("Enter the event name:")

if st.button("Find Outfit"):
    prompt = f"What did {celebrity_name} wear to {event_name}?"
    result = generate_text(prompt, api_key)
    st.write(result)

    keywords = extract_keywords(result)
    if len(keywords) > 0:
        st.write("Keywords found in the text:")
        for keyword in keywords:
            st.write(f"- {keyword}")
    else:
        st.write("No keywords found in the text.")
