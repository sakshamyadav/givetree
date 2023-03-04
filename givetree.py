import openai
import streamlit as st

# Define function to extract information from text
def extract_information(input_text, information, api_key):
    openai.api_key = api_key
    prompt = (f"Extract the {information} from the following text:\n\n"
              f"{input_text}\n\n"
              f"The {information} is:")
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
def app():
    # Set app title
    st.title("What Did They Wear?")

    # Set up input form
    api_key = st.text_input("Enter your OpenAI API key:")
    celebrity_name = st.text_input("Enter the name of the celebrity:")
    event_name = st.text_input("Enter the name of the event:")
    input_text = st.text_input("Enter the text to extract information from:")
    information = st.selectbox("Select the information to extract:", ["Dress", "Shoes", "Jewelry", "All"])

    # Extract information on button click
    if st.button("Extract Information"):
        if not api_key:
            st.warning("Please enter your OpenAI API key.")
        elif not celebrity_name:
            st.warning("Please enter the name of the celebrity.")
        elif not event_name:
            st.warning("Please enter the name of the event.")
        elif not input_text:
            st.warning("Please enter some text to extract information from.")
        elif information == "All":
            dress = extract_information(input_text, "dress", api_key)
            shoes = extract_information(input_text, "shoes", api_key)
            jewelry = extract_information(input_text, "jewelry", api_key)
            st.write(f"{celebrity_name} wore {dress}, paired with {shoes} and {jewelry} at {event_name}.")
        else:
            extracted_info = extract_information(input_text, information.lower(), api_key)
            st.write(f"{celebrity_name} wore {extracted_info} at {event_name}.")
