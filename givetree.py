import streamlit as st
import openai

def generate_text(prompt, api_key):
    openai.api_key = api_key
    model_engine = "davinci"
    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=2048, 
                                            n=1,stop=None,temperature=0.7)
    message = completions.choices[0].text
    return message.strip()

st.title("Celebrity Outfit Finder")

api_key = st.text_input("Enter your OpenAI API key:")
celebrity_name = st.text_input("Enter the celebrity name:")
event_name = st.text_input("Enter the event name:")

if st.button("Find Outfit"):
    prompt = f"What did {celebrity_name} wear to {event_name}?"
    result = generate_text(prompt, api_key)
    st.write(result)

    # Extract entities from the generated text
    openai.api_key = api_key
    model_engine = "davinci"
    completions = openai.Completion.create(engine=model_engine, prompt=result, max_tokens=2048,
                                            n=1,stop=None,temperature=0.7, 
                                            model="text-davinci-002", 
                                            model_output_prefix="ENTITIES:\n")
    entities_text = completions.choices[0].text
    entities = entities_text.split("\n")[1:-1]
    if len(entities) > 0:
        st.write("Entities found in the text:")
        for entity in entities:
            st.write(f"- {entity}")
    else:
        st.write("No entities found in the text.")
