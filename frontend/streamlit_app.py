import io
from datetime import datetime
from tzlocal import get_localzone
import streamlit as st
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair

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

    # Define the scan intervals in 24 hour format
    scan_intervals = [(0, 6), (6, 12), (12, 18), (18, 24)]

    # Find which interval the current time falls into
    for start, end in scan_intervals:
        if start <= current_date_time.hour < end:
            # Format the start and end times for the output
            start_time = datetime(current_date_time.year, current_date_time.month, current_date_time.day, start)
            end_time = datetime(current_date_time.year, current_date_time.month, current_date_time.day, end)
            break
    else:
        # If the time is between 0 and 6, the scan happened on the previous day between 18 and 24
        start_time = datetime(current_date_time.year, current_date_time.month, current_date_time.day, 18) - timedelta(days=1)
        end_time = datetime(current_date_time.year, current_date_time.month, current_date_time.day, 0)

    file_content = "\n"
    for line in lines:
        file_content += line + "\n"

    output_space.markdown(f'The trend scanning, executed at {formatted_date_time} ({timezone_name}), fell within the scanning interval from {start_time.strftime("%Y-%m-%d %H:%M:%S")} to {end_time.strftime("%Y-%m-%d %H:%M:%S")}. During this period, we identified 4 pieces of important news and 1 item of news with long-term impact, as outlined below: \n{file_content}')
    
elif talk_clicked:
    output_space.write(f'PulsarWave is talking...')
elif input_query_clicked:
    if user_input:  # check if user_input is not empty
        context = """you\'re a geopolitical expert and ready to provide your analysis to the user as he is the C-Suit director."""
        response = process_text(user_input, context, 256)
        output_space.write(f"Response from Model: {response.text}")
    else:  # if user_input is empty
        output_space.write(f"Hello, I am your geopolitical expert assistant. How can I help you today?")



