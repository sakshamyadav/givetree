import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# Set up the Streamlit app
st.title("Text to Art Tool")

# Define the input fields for the Streamlit app
text = st.text_input("Enter your text here")
num_images = st.number_input("Number of images to generate", value=1, min_value=1, max_value=10)
api_key = st.text_input("Enter your OpenAI API key")

# Generate the text art using the OpenAI DALL-E API
if st.button("Generate Text Art"):
    # Send a POST request to the OpenAI DALL-E API with the input text and desired number of images
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}" # Use the API key entered by the user
        },
        json={
            "model": "image-alpha-003", # DALL-E model to use
            "prompt": f"Generate an image of '{text}'",
            "num_images": num_images,
            "size": "1024x1024",
            "response_format": "url"
        }
    )

    # Display the generated text art
    if response.status_code == 200:
        results = response.json()["data"]
        for result in results:
            image_url = result["url"]
            image_bytes = requests.get(image_url).content
            image = Image.open(BytesIO(image_bytes))
            st.image(image, caption="Text Art", use_column_width=True)
    else:
        st.error("Error generating text art. Please try again.")
