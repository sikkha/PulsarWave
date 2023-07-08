import streamlit as st
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

vertexai.init(project="flaskgeopolitics", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
chat = chat_model.start_chat(
    context="""you\'re a geopolitical expert and ready to provide your analysis to the dead of the user as he is the C-Suit director.""",
)


def count_words(input_text):
    words = input_text.split(' ')
    num_words = len(words)
    return num_words

# Display the logo at the top of the page 
#st.image("../main/NewPulsarWave_logo.png")

st.title('Please ask your PulsarWave')

user_input = st.text_input("What's up today?")

# Save a reference to the button click events
col1, col2, col3, col4 = st.columns(4)
count_words_clicked = col1.button('Count Words')
trend_scan_clicked = col2.button('Trend Scan')
talk_clicked = col3.button('Talk!')
input_query_clicked = col4.button('Input query')

# Put a line after the buttons
st.markdown("---")

# Create a placeholder for the output
output_space = st.empty()

# Check which button was clicked and write to the output space
if count_words_clicked:
    word_count = count_words(user_input)
    output_space.write(f'The text contains {word_count} words.')
elif trend_scan_clicked:
    output_space.write(f'Scan Radar is working...')
elif talk_clicked:
    output_space.write(f'Robot is talking...')
elif input_query_clicked:
    response = chat.send_message(user_input, **parameters)
    #print(f"Response from Model: {response.text}")
    output_space.write(f"Response from Model: {response.text}")

