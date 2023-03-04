import openai
import streamlit as st

# Define function to extract information from text
def extract_information(celebrity_name, event_name,information, api_key):
    openai.api_key = api_key
    prompt = (f"Extract the {information} from the following text:\n\n"
              f"What {information} did {celebrity_name} wear at {event_name}")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=200,
        n=1,
        stop=None,
        timeout=15,
    )
    return response.choices[0].text.strip()

# Define Streamlit app
# Set app title
st.title("What Did They Wear?")

# Set up input form
api_key = st.text_input("Enter your OpenAI API key:")
celebrity_name = st.text_input("Enter the name of the celebrity:")
event_name = st.text_input("Enter the name of the event:")
information = st.selectbox("Select the information to extract:", ["Dress", "Shoes", "Jewelry", "All"])

# Extract information on button click
if st.button("Extract Information"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not celebrity_name:
        st.warning("Please enter the name of the celebrity.")
    elif not event_name:
        st.warning("Please enter the name of the event.")
    else:
        extracted_info = extract_information(celebrity_name, event_name, information.lower(), api_key)
        st.write(f"{celebrity_name} wore {extracted_info} at {event_name}.")
