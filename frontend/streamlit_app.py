import io
from datetime import datetime
from tzlocal import get_localzone
import streamlit as st
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from google.cloud import texttospeech

def process_text(user_input, context, maxtoken, project="flaskgeopolitics", location="us-central1"):
    # initialize
    vertexai.init(project=project, location=location)
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    
    # parameters
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": maxtoken,
        "top_p": 0.8,
        "top_k": 40
    }
    
    # start chat
    chat = chat_model.start_chat(context=context)
    
    # send message and get response
    response = chat.send_message(user_input, **parameters)

    # return response
    return response

def escape_markdown(text):
    # Add more special characters to the list if needed
    for special_char in ['*', '_', '#']:
        text = text.replace(special_char, '\\' + special_char)
    return text


def count_words(input_text):
    words = input_text.split(' ')
    num_words = len(words)
    return num_words

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    return response.audio_content



# Display the logo at the top of the page 
st.image("./siu.png")




st.title('Please ask your PulsarWave')

user_input = st.text_input("What's up today?")

# Save a reference to the button click events
col1, col2, col3, col4 = st.columns(4)
weekly_report_clicked = col1.button('Weekly Report')
trend_scan_clicked = col2.button('Trend Scan')
talk_clicked = col3.button('Talk!')
input_query_clicked = col4.button('Input query')

# Put a line after the buttons
st.markdown("---")

# Create a placeholder for the output
output_space = st.empty()

# Check which button was clicked and write to the output space
if weekly_report_clicked:
    #word_count = count_words(user_input)
    file_content = read_file('/tmp/superb.txt')
    context = """you\'re a geopolitical expert and your job is to refine and revised the draft of report from the intelligence department in order to submit to the user as he is the C-Suit director. Please use your internet accessing ability to verify it, revising it to conform the retrieval information is allowed. Mark the report with colorful emoji you see fit."""
    response = process_text(file_content, context, 500)
    output_space.write(f"Response from Model: {response.text}")

    # Display additional text and a clickable link
    st.write("You can access our weekly Trend Monitoring Radar (TMR) at the link below:")
    st.markdown("[http://www.geopolitics.io](http://www.geopolitics.io)")
elif trend_scan_clicked:
    with open('/tmp/sixhour_scan.txt', 'r') as file:
        lines = file.readlines()

    # Get the current date and time
    current_date_time = datetime.now()

    local_tz = get_localzone()

    # Get the timezone name
    timezone_name = current_date_time.astimezone(local_tz).strftime("%Z")

    # Format the date and time
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")


    file_content = "\n"
    for line in lines:
        file_content += line + "\n"

    output_space.markdown(f'The trend scanning was executed at {formatted_date_time} ({timezone_name}). During this period, we identified 4 pieces of important news and 1 item of news with long-term impact, as outlined below: \n{file_content}')

elif talk_clicked:
    output_space.write(f'Pulsarwave is in the process of preparing the audio transcript...')
    file_content = read_file('/tmp/sixhour_scan.txt')
    context = """you\'re a geopolitical expert and your job is to summarize the input from the user in briefing manner within two paragraph. Please print only the summarization."""
    response = process_text(file_content, context, 400)
    output_space.write(f"Response from Model: \n {response.text}")
    audio_content = synthesize_text(response.text)
    st.audio(audio_content, format='audio/mp3')




elif input_query_clicked:
    # Get the current date and time
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

    if user_input:  # check if user_input is not empty
        context = """The current time is {current_date_time}. You\'re a geopolitical expert and ready to provide your analysis to the user as he is the C-Suit director."""
        response = process_text(user_input, context, 256)
        output_space.write(f"Response from Model: {response.text}")
    else:  # if user_input is empty
        output_space.write(f"Hello, I am your geopolitical expert assistant. How can I help you today?")

