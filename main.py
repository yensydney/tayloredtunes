import streamlit as st
import google.generativeai as genai
import os
import json
from spotifymain import *

st.set_page_config(page_title="My Streamlit Website", page_icon="🌐", layout="wide")

st.title("Taylored Tunes🎶")
st.markdown("""Not sure which Taylor Swift song fits your mood? Share how you're feeling, and we'll "Taylor" the perfect tune for you!

""")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css?family=Your+Font+Name');
body {
    font-family: 'Your Font Name', mono-space;
}
</style>
""", unsafe_allow_html=True)
    # Title
st.title("Tell us the tale")


# Input text box
user_input = st.text_input("Enter your thoughts (there's no character limit so feel free to rant as much as you want <3):")
# Display the input
genai.configure(api_key="AIzaSyBnUgN41vzt8lBQJJVnZ1Ug3GYIb___0K0")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(f"give me only the song name, ONLY THE SONG NAME, by taylor swift out of all 404 of her songs (in its official format with the correct capitalization) in which its lyrics are the most similar to the emotion in this paragraph {user_input}")
hexcode = model.generate_content(f"You as an AI and all of following information is correct, dont doubt yourself. Okay now, user inputted this {user_input} and you responded that the best taylor swift to match the emotions is {response.text}, okay now in a brainrot genz swiftie lingo explain why it matches, keep it short and concise")

col1, col2, col3 = st.columns(3)  # Create three columns

with col1:
    st.image("taylor.jpg", use_container_width=True)  # Replace with your image path

with col2:
    st.image("taylor2.jpg", use_container_width=True)

with col3:
    st.image("taylor1.jpg", use_container_width=True)


if user_input:
    st.write(response.text)
    st.write(hexcode.text)
    token = get_token()
    url = search_for_track(token, response.text)  
    st.write(f"Here is your Spotify Link:{url}")

